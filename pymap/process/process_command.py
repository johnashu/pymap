import subprocess
from pymap.includes.config import *
from typing import Tuple


class RunProcess:
    def run_method(
        self, method: str, context: dict, args: list = [], prog: str = marker, std_in: str = ''
    ) -> Tuple[bool, str]:
        if not context:
            return False, "No context provided"
        command_list = [os.path.join(envs.binaries, prog), method]
        for k, v in context.items():
            if k not in ignore:
                command_list += [f"--{k}", f"{v}"]
        if args:
            command_list += args

        command_list = [x for x in command_list if x]

        log.info(command_list)
        log.info(" ".join(command_list))

        try:
            p = subprocess.Popen(
                command_list,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                universal_newlines=True,
            )

            if std_in:
                res = p.communicate(input=std_in)[0]
            
            log.info(p.communicate()[0])
            log.info(p.communicate()[1])
        except subprocess.SubprocessError as e:
            log.error(e)

        return True, res
