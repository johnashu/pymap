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
            5: self.unlock_map,
            6: self.get_account_nonvoting_locked_gold,
            7: self.get_pending_withdrawals,
            8: self.withdraw_map,
            9: self.register,
            10: self.deregister,
            11: self.revert_register,
            12: self.authorise_validator_signer,
            13: self.vote,
            14: self.activate_votes,
            15: self.revoke_pending_votes,
            16: self.revoke_active_votes,
            17: self.join_network,
            18: self.make_ECDSA_signature_from_signer,
            19: self.make_BLS_proof_of_possession_from_signer,
            20: self.get_balance,
            21: self.check_if_selected,
            999: self.reboot_server,
        }
        while True:
            os.system("clear")
            self.display_from_file(main_menu)
            try:
                option = int(input("Enter your option: "))
            except ValueError:
                os.system("clear")
                self.error_input()
                self.run_full_node()
            try:
                menu_options[option]()
            except KeyError:
                print('Option not found, Please enter a choice from the menu')
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
