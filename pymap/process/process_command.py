from pymap.includes.config import *
from typing import Tuple
import asyncio
import logging

class RunProcess:
    
    attach_prompt_found = False

    async def watch(
        self,
        stream,
        prefix: str = ">",
        save_keystore: bool = False,
        scrolling: bool = False,
        isSigner: bool = False,
        isAttach: bool = False,
    ):
        async for line in stream:
            l = line.decode().strip()
            l_split = l.split(":")
            if save_keystore:                
                if l_split[0].endswith("secret key file"):
                    if isSigner:
                        self.signer_keystore = l_split[-1].strip()
                    else:
                        self.keystore = l_split[-1].strip()
                self.update_env(self.base_field_keys)

            if isAttach:
                if self.attach_prompt_found:
                    log.info(f"{prefix}: {l}")
                    self.attach_prompt_found = False
                if l == '>':
                    self.attach_prompt_found = True

                # if l_split[0].endswith('block'):
                #     log.info(f"Block Number of Node:  {l_split[1].split()[0]}")
            else:
                if not scrolling:
                    log.info(f"{prefix}  {l}")
                else:
                    print(f"{prefix}  {l}")

    async def create_process(self, cmd):

        p = await asyncio.create_subprocess_exec(
            *cmd,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        return p

    async def run(self, cmd, std_in: str = "", **kw):
        p = await self.create_process(cmd)
        if std_in:
            p.stdin.write(std_in)
        await asyncio.gather(
            self.watch(
                p.stdout,
                **kw,
            ),
            self.watch(
                p.stderr,
                **kw,
            ),
        )

    def run_method(
        self,
        method: str,
        context: dict,
        args: list = [],
        prog: str = marker,
        std_in: str = "",
        **kw,
    ) -> Tuple[bool, str]:

        if isinstance(method, str):
            method = [method]

        command_list = [os.path.join(envs.binaries, prog) if prog else ""] + method
        for k, v in context.items():
            if k not in ignore:
                if v:
                    command_list += [f"--{k}", f"{v}"]

        if args:
            command_list += args

        command_list = [x for x in command_list if x]

        # log.info(command_list)

        cmd_to_process = " ".join(command_list)

        log.info(
            f"{self.print_stars}\n\nCommand to Process:\n\n\t{cmd_to_process}\n\n{self.print_stars}"
        )

        try:
            logging.getLogger("asyncio").setLevel(logging.CRITICAL)
            asyncio.run(self.run(command_list, bytes(std_in, "utf-8"), **kw))
        except KeyboardInterrupt:
            pass
