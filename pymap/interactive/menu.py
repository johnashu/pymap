import os
from colorama import Fore
from pymap.tools.utils import askYesNo
from pymap.methods.marker_methods import MarkerMethods


class Menu(MarkerMethods):
    def __init__(self, **base_fields: dict) -> None:
        super(Menu, self).__init__(**base_fields)

    def is_testnet(self) -> None:
        while 1:
            try:
                testnet = int(
                    input(
                        "Please indicate if you wish to use Testnet or Mainnet\n\t* [1] Testnet\n\t* [2] Mainnet\n\t>>> "
                    )
                )
                if testnet in (1, 2):
                    break
            except ValueError:
                pass
        if testnet == 1:
            self.base_context.update(
                {
                    "rpcaddr": self.testnet,
                }
            )
            self.rpcaddr = self.testnet

    def run_full_node(self) -> None:
        self.is_testnet()
        while True:
            os.system("clear")
            self.create_menu()
            try:
                option = int(input("Enter your option: "))
                try:
                    self.menu[option]()
                except KeyError as e:
                    print(e)
                    print("Option not found, Please enter a choice from the menu")
                input("Press Enter to show menu or CTRL+C to exit..")
            except ValueError:                
                self.error_input()

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
            os.system("sudo service atlasNode stop")
            os.system("sudo reboot")
        else:
            print("Invalid option.")
