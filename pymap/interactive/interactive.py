import os
import logging as log
from pymap.interactive.menu import Menu
from pymap.tools.key_from_keystore import pk_from_store
from pymap.tools.block_epoch_utils import get_current_epoch, time_to_next_block


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
        msg = f"""
        Local Block Number: {local_block}
        RPC Block Number:   {rpc_block}
        Blocks Synced:      {self.red_or_green(match)}        
        """
        print(self.star_surround(msg))

    def get_epoch_data(self) -> None:
        current_block = int(self.get_block_number())
        bpe = int(self.blocks_per_epoch)
        t, epoch, next_epoch = time_to_next_block(current_block, bpe)
        msg = f"""
        Current Block: {current_block}

        Current Epoch: {epoch}
        
        Next Epoch:    {epoch+1} starts @ block {next_epoch} in {t.days} day(s) | {t.hours} hour(s) | {t.minutes} min(s) | {t.seconds} sec(s)
        """
        print(self.star_surround(msg))

    def start(self) -> None:
        self.intro_message()
        self.run_full_node()
