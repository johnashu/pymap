import subprocess
from pymap.includes.config import *
from typing import Tuple
import asyncio
import logging
import shlex


class RunProcess:
    async def watch(self, stream, prefix="", save_keystore: bool = False):
        async for line in stream:
            l = line.decode().strip()
            if save_keystore:
                ks = l.split(":")
                if ks[0].endswith("secret key file"):
                    self.keystore = ks[-1].strip()
                    self.update_env(self.base_field_keys)
            log.info(f"{prefix}  {l}")

    async def create_process(self, cmd):

        p = await asyncio.create_subprocess_exec(
            *cmd,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        return p

    async def run(self, cmd, std_in: str = "", save_keystore: bool = False):
        p = await self.create_process(cmd)
        if std_in:
            p.stdin.write(std_in)
        await asyncio.gather(
            self.watch(p.stdout, "INFO:", save_keystore=save_keystore),
            self.watch(p.stderr, "ERROR:", save_keystore=save_keystore),
        )

    def run_method(
        self,
        method: str,
        context: dict,
        args: list = [],
        prog: str = marker,
        std_in: str = "",
        shell: bool = False,
        save_keystore: bool = False,
        return_command: bool = False,
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
            asyncio.run(
                self.run(
                    command_list, bytes(std_in, "utf-8"), save_keystore=save_keystore
                )
            )
        except KeyboardInterrupt:
            pass
