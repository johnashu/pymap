from turtle import update
from pymap.interactive.menu import Menu
from pymap.tools.key_from_keystore import pk_from_store
import os


class InteractiveSetup(Menu):
    def __init__(self, **base_fields: dict) -> None:
        super(InteractiveSetup, self).__init__(**base_fields)

    def backup_env(self) -> None:
        fn = input(
            "Please Enter Backup Location and Filename, i.e. /home/backup.env : "
        )
        self.update_env(self.base_field_keys, fn)

    def find_pk(self, isSigner: bool = False) -> None:
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
                self.handle_input({cur_list[choice]: str()})
            except ValueError:
                self.error_input()

    def start(self) -> None:
        self.intro_message()
        self.run_full_node()
