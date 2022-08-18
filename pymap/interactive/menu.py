import os
from colorama import Style, Fore, Back
from pymap.tools.file_op import open_file
from pymap.tools.utils import askYesNo
from pymap.includes.config import main_menu
from pymap.methods.run_method import Methods


class Menu(Methods):
    def __init__(self, **base_fields: dict) -> None:
        super(Menu, self).__init__(**base_fields)

    def menu_reset(self) -> None:
        print(Style.RESET_ALL)
        for x in open_file(main_menu):
            x = x.strip()
            try:
                x = eval(x)
            except SyntaxError:
                pass
            if x:
                print(x)

    def run_full_node(self) -> None:
        menu_options = {
            0: self.finish_node,
            1: self.get_total_votes_for_eligible_validator,
            2: self.new_validator,
            3: self.create_account,
            4: self.locked_map,
            5: self.authorise_validator_signer,
            6: self.vote,
            999: self.reboot_server,
        }
        while True:
            self.menu_reset()
            try:
                option = int(input("Enter your option: "))
            except ValueError:
                os.system("clear")
                self.whitespace()
                self.stars(reset=1)
                print(
                    "* "
                    + Fore.RED
                    + "WARNING"
                    + Style.RESET_ALL
                    + ": Only numbers are possible, please try your selection on the main menu once again."
                )
                self.stars(reset=1)
                self.whitespace()
                input("* Press ENTER to return to the main menu")
                self.run_full_node()
            os.system("clear")
            menu_options[option]()

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
