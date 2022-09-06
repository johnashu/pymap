import logging as log
import os
from colorama import Style, Fore, Back
from pymap.tools.utils import askYesNo
from pymap.tools.utils import take_input, is_signer
from pymap.tools.file_op import save_file
from pymap.includes.mappings.names import name_map


class HandleInput:
    def __init__(self, reset: int = 0, **kw):
        super(HandleInput, self).__init__()

    def update_env(self, keys: list, fn=".env") -> None:
        to_write = ""
        for k in keys:
            line = f"{k}={self.__dict__[k]}\n"
            to_write += line
        save_file(os.path.join(os.getcwd(), fn), to_write)

    def handle_input(
        self,
        context: dict,
        remove: tuple = (),
        signer_fields: tuple = (),
        ask_is_signer: bool = False,
        isSigner: bool = False,
        allow_empty: bool = False,
    ) -> None:
        if ask_is_signer:
            isSigner = is_signer()

        if remove:
            context = {k: v for k, v in context.items() if k not in remove}
            
        for k, v in context.items():
            if k in self.miner_flags:
                continue

            key = k
            if isSigner:
                if k in signer_fields:
                    key = f"signer_{k}"
            try:
                arg = self.__dict__[key]
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
                    allow = False
                    if allow_empty:
                        allow = askYesNo(
                            "* "
                            + Fore.RED
                            + " WARNING "
                            + Style.RESET_ALL
                            + "Are you sure you want to"
                            + Fore.RED
                            + " DELETE "
                            + Style.RESET_ALL
                            + "this Field?"
                        )

                    if not allow:
                        i = self.__dict__[key]
                    else:
                        self.__dict__[key] = i
                except KeyError as e:
                    log.error(f"Argument not found for {k}  ::  {e}")
            else:
                self.__dict__[key] = i
            context[k] = i
        self.update_env(self.base_field_keys)
        # toggle between name (mainnet) and namePrefix (testnet)
        # Will be removed when testnet is updated.
        # --namePrefix change to --name in v1.2.1
        if self.testnet == self.rpcaddr and context.get("name"):
            context["namePrefix"] = context.get("name")
            if context.get("name"):
                del context["name"]

        return context
