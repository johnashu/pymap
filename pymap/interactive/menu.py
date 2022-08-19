import os
from colorama import Style, Fore
from pymap.tools.utils import askYesNo
from pymap.includes.config import main_menu
from pymap.methods.marker_methods import MarkerMethods


class Menu(MarkerMethods):
    def __init__(self, **base_fields: dict) -> None:
        super(Menu, self).__init__(**base_fields)

    def run_full_node(self) -> None:
        menu_options = {
            0: self.finish_node,
            1: self.get_total_votes_for_eligible_validator,
            2: self.new_validator,
            3: self.create_account,
            4: self.locked_map,
            5: self.register,
            6: self.deregister,
            7: self.revert_register,
            8: self.authorise_validator_signer,
            9: self.vote,
            10: self.activate_votes,
            11: self.revoke_pending_votes,
            12: self.revoke_active_votes,
            13: self.join_network,
            14: self.make_ECDSA_signature_from_signer,
            15: self.make_BLS_proof_of_possession_from_signer,
            999: self.reboot_server,
        }
        while True:
            self.display_from_file(main_menu)
            try:
                option = int(input("Enter your option: "))
            except ValueError:
                os.system("clear")
                self.error_input()
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
