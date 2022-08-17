import subprocess
from pymap.includes.config import *
from typing import Tuple


class RunProcess:
    def run_method(self, method: str, context: dict) -> Tuple[bool, str]:
        if not context:
            return False, "No context provided"
        command_list = [prog, method]
        for k, v in context.items():
            command_list += [f"--{k}", v]

        log.info(command_list)

        res = subprocess.run(
            command_list,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            universal_newlines=True,
        )

        log.info(res.stderr)
        log.info(res.stdout)

        return True, res
