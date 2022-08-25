import logging as log
import os
from pymap.tools.utils import take_input
from pymap.tools.file_op import save_file
from pymap.includes.mappings.names import name_map


class HandleInput:
    def __init__(self, reset: int = 0, **kw):
        super(HandleInput, self).__init__()

    def update_env(self, keys: list) -> None:
        to_write = ""
        for k in keys:
            line = f"{k}={self.__dict__[k]}\n"
            to_write += line
        save_file(os.path.join(os.getcwd(), ".env"), to_write)

    def handle_input(self, context: dict) -> None:
        # local = {k: v for k, v in context.items() if k not in self.base_fields}
        for k, v in context.items():
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
            context[k] = i
        print(self.base_field_keys)
        self.update_env(self.base_field_keys)
        return context
