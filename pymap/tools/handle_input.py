from pymap.tools.utils import take_input
from pymap.includes.mappings.names import name_map
import logging as log


class HandleInput:
    def __init__(self, reset: int = 0, **kw):
        super(HandleInput, self).__init__()

    def handle_input(self, context: dict) -> None:
        local = {k: v for k, v in context.items() if k not in self.base_fields}
        for k, v in local.items():
            try:
                arg = self.__dict__[k]
            except KeyError:
                arg = ""

            display = (
                " ".join(k.split("_")).title()
                if not name_map.get(k)
                else name_map.get(k)
            )
            i = take_input(type(v), f"Please Enter {display} ({arg}): ")
            if not i:
                try:
                    i = self.__dict__[k]
                except KeyError as e:
                    log.error(f"Argument not found for {k}  ::  {e}")
            else:
                self.__dict__[k] = i
            local[k] = i
        return local
