import subprocess
from pymap.includes.config import *
from typing import Tuple


class RunProcess:
    def run_method(
        self, method: str, context: dict, args: list = [], prog: str = marker
    ) -> Tuple[bool, str]:
        if not context:
            return False, "No context provided"
        command_list = [os.path.join(envs.binaries, prog), method]
        for k, v in context.items():
            if k not in ignore:
                command_list += [f"--{k}", f"{v}"]
        if args:
            command_list += args

        log.info(command_list)
        log.info(" ".join(command_list))

        try:
            res = subprocess.run(
                command_list,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
                universal_newlines=True,
            )

            log.info(res.stderr)
            log.info(res.stdout)
        except subprocess.SubprocessError as e:
            log.error(e)

        return True, res
