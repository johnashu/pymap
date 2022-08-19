import subprocess
from pymap.includes.config import *
from typing import Tuple


class RunProcess:
    def run_method(
        self,
        method: str,
        context: dict,
        args: list = [],
        prog: str = marker,
        std_in: str = "",
        shell=False,
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

        log.info(f'Command to Process:\n\t{" ".join(command_list)}')

        try:
            p = subprocess.Popen(
                command_list,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                universal_newlines=True,
                shell=shell,
            )

            if std_in:
                p.communicate(input=std_in)[0]
            else:
                p.communicate(input="\n")[0]

            out, err = p.communicate()

            log.info(out)
            log.error(err)
        except (FileNotFoundError, subprocess.SubprocessError) as e:
            log.error(e)
            return False, (command_list, e)

        return True, (out, err)
