import os
from colorama import Fore
from pymap.tools.utils import askYesNo
from pymap.methods.marker_methods import MarkerMethods


class Menu(MarkerMethods):
    def __init__(self, **base_fields: dict) -> None:
        super(Menu, self).__init__(**base_fields)

    def run_full_node(self) -> None:
        while True:
            os.system("clear")
            self.create_menu()
            try:
                option = int(input("Enter your option: "))
            except ValueError:
                os.system("clear")
                self.error_input()
                self.run_full_node()
            try:
                self.menu[option]()
            except KeyError:
                print("Option not found, Please enter a choice from the menu")
            input("Press Enter to show menu or CTRL+C to exit..")

    def finish_node(self):
        self.stars()
        print("* Thanks for using the tool! Goodbye.")
        self.stars()
        raise SystemExit(0)

    def reboot_server(self) -> str:
        self.stars(reset=1)
        question = askYesNo(
            Fore.RED
            + "WARNING: YOU WILL MISS BLOCKS WHILE YOU REBOOT YOUR ENTIRE SERVER.\n\n"
            + "Reconnect after a few moments & Run the Validator Toolbox Menu again\n"
            + Fore.WHITE
            + "Are you sure you would like to proceed with rebooting your server?\n\nType 'Yes' or 'No' to continue"
        )
        if question:
            os.system("sudo reboot")
        else:
            print("Invalid option.")
