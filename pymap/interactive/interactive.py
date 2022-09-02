from pymap.interactive.menu import Menu
from pymap.tools.key_from_keystore import pk_from_store
import os
import logging as log


class InteractiveSetup(Menu):
    def __init__(self, **base_fields: dict) -> None:
        super(InteractiveSetup, self).__init__(**base_fields)

    def backup_env(self) -> None:
        fn = input(
            "Please Enter Backup Location and Filename, i.e. /home/backup.env : "
        )
        self.update_env(self.base_field_keys, fn)

    def find_pk(self) -> None:
        context = {"keystore": self.keystore, "password": self.password}
        context.update(self.handle_input(context))
        pk_from_store(self.keystore, self.password)

    def display_and_update_env(self) -> None:
        while 1:
            os.system("clear")
            cur_list = self.list_envs()
            try:
                choice = int(
                    input(
                        "\nTo update an item, please select a number or press 0 to go back:  "
                    )
                )
                if choice == 0:
                    break
                self.handle_input({cur_list[choice]: str()}, allow_empty=True)
            except ValueError:
                self.error_input()

    def compare_block_numbers(self) -> None:
        self.get_eth_block_number_from_node()
        rpc_block = int(self.get_block_number())      
        local_block = int(self.local_block)
        match = local_block == rpc_block
        msg = f'Local Block Number: {local_block:>20}\nRPC Block Number:{rpc_block:>20}\nRPC Block == Local Block Number?:  {self.red_or_green(match)}'

        log.info(self.star_surround(msg))

    def start(self) -> None:
        self.intro_message()
        self.run_full_node()
