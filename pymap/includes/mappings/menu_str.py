menu_items = {
    "Check Vote Statistics": "get_total_votes_for_eligible_validator",
    "Create New Wallet": "new_validator",
    "Çreate New Account": "create_account",
    "Lock Map": "locked_map",
    "Unlock Map": "unlock_map",
    "Get Account Non Voting Locked Maps": "get_account_nonvoting_locked_gold",
    "Get Account Total Locked Maps": "get_account_total_locked_gold",
    "Get Active Votes for Validator by Account": "get_active_votes_for_validator_by_account",
    "Get Pending Withdrawals": "get_pending_withdrawals",
    "Withdraw Map": "withdraw_map",
    "Register Validator": "register",
    "De-Register Validator": "deregister",
    "Revert Register Validator": "revert_register",
    "Authorise Signer": "authorise_validator_signer",
    "Vote": "vote",
    "Activate Votes": "activate_votes",
    "Revoke Pending Votes": "revoke_pending_votes",
    "Revoke Active Votes": "revoke_active_votes",
    "Join Network (Sync)": "join_network",
    "Make ECDSA Signature From Signer": "make_ECDSA_signature_from_signer",
    "Make BLS Proof Of Possession From Signer": "make_BLS_proof_of_possession_from_signer",
    "Get Balance": "get_balance",
    "Check if Elected": "check_if_selected",
    "Private Key From Keystore": "find_pk",
}

from colorama import Fore, Back, Style


class M:

    menu = {
        0: "finish_node",
        999: "reboot_server",
    }

    def create_menu(self):
        msg = (
            Fore.YELLOW
            + Back.RED
            + "WARNING: You may miss blocks during a reboot!"
            + Style.RESET_ALL
        )
        print("*  Map Validator Menu Options:")
        print("*")
        for i, k in enumerate(menu_items.keys()):
            print(f"*  [{i+1}] {k}")
            # self.menu[i+1] = eval(f'self.{menu_items[k]}')
        print(
            f"""
        
*********************************************************************************************
print("*[999] Reboot Server             - {msg}
print("*  [0] Exit Application          - Goodbye!")
*********************************************************************************************
        """
        )


m = M()
m.create_menu()
print(m.menu)
