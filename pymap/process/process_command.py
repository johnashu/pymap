from pymap.includes.config import *
from typing import Tuple
import asyncio
import logging

from pymap.tools.utils import readable_price


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
        isECDSA: bool = False,
        localBlock: bool = False,
        attachValue: int = 0,
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
            if isECDSA:
                if l.split("=")[0].endswith("result"):
                    self.signature = l.split("=")[-1].strip()
            self.update_env(self.base_field_keys)

            if isAttach:
                if self.attach_prompt_found:
                    self.__dict__[attachValue] = l
                    if localBlock:
                        l = readable_price(l, d=0, show_decimals=False)
                    print(f"{prefix}: {l}")
                    self.attach_prompt_found = False
                    return
                if l == ">":
                    self.attach_prompt_found = True
            else:
                if not scrolling:
                    log.info(f"{prefix}  {l}")
                else:
                    print(f"{prefix}  {l}")

    async def create_process(self, cmd):

        return await asyncio.create_subprocess_exec(
            *cmd,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

    async def run(self, cmd, std_in: str = "", **kw):

        p = await self.create_process(cmd)

        if std_in:
            p.stdin.write(std_in)
        if kw.get("isAttach"):
            p.stdin.close()
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
                if v or k in self.miner_flags:
                    command_list += [f"--{k}", f"{v}"]

        if args:
            command_list += args

        command_list = [x for x in command_list if x]

        # print(command_list)

        cmd_to_process = " ".join(command_list)
        msg = f"Command to Process:\n\n\t{cmd_to_process}"
        self.star_surround(msg)

        try:
            logging.getLogger("asyncio").setLevel(logging.CRITICAL)
            asyncio.run(self.run(command_list, bytes(std_in, "utf-8"), **kw))
        except KeyboardInterrupt:
            pass
