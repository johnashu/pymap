from pymap.tools.utils import take_input
import logging as log


class HandleInput:
    def __init__(self, reset: int = 0, **kw):
        super(HandleInput, self).__init__()

    def handle_input(self, context: dict) -> None:
        local = {k: v for k, v in context.items() if not v}
        for k, v in local.items():
            print(k, type(v))
            try:
                arg = eval(f"self.{k}")
            except AttributeError:
                arg = ""
            i = take_input(
                type(v), f"Please Enter {' '.join(k.split('_')).title()} ({arg}): "
            )
            print(arg, i)
            if not i:
                try:
                    i = eval(f"self.{k}")
                except AttributeError as e:
                    log.error(f"Argument not found for {k}  ::  {e}")
            else:
                exec(f"self.{k} = {i}")
            local[k] = i
            print(local)

        print(local)
        return local
