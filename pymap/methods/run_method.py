from pymap.process.process_command import RunProcess
from pymap.interactive.display import PrintStuff
from pymap.tools.utils import take_input


class Methods(RunProcess, PrintStuff):

    base_fields = ("rpcaddr", "rpcport", "keystore", "password")

    def __init__(self, **base_fields: dict) -> None:
        self.set_fields(**base_fields)
        self.base_context = {
            k: v for k, v in base_fields.items() if k in self.base_fields
        }
        print(self.rpcaddr)
        super(Methods, self).__init__(**base_fields)

    def set_fields(self, **base_fields) -> None:
        for k, v in base_fields.items():
            setattr(self, k, str(v))

    def new_validator(self, datadir: str = "") -> None:
        if not datadir:
            datadir = take_input(str, "Enter Directory to save keystore: ")
            password = take_input(str, "Enter Keystore password: ")
        args = ["account", "new"]
        context = {"datadir": datadir}
        self.run_method("", context, args=args, prog="atlas", std_in = password)

    def create_account(self) -> None:
        """
        https://docs.maplabs.io/develop/map-relay-chain/marker/aboutcommon#createaccount
        """

        context = {**self.base_context, **{"namePrefix": "validator"}}
        self.run_method("createAccount", context)

    def locked_map(self, locked_num: int = 0) -> None:
        # Lock MAP in Validator - Stake
        if locked_num == 0:
            locked_num = take_input(int, "Enter amount of MAP to lock: ")
        context = {**self.base_context, **{"lockedNum": locked_num}}
        self.run_method("lockedMAP", context)

    def authorise_validator_signer(self, signer_pkey: str = "") -> None:
        if not signer_pkey:
            signer_pkey = take_input(str, "Enter Signer Private Key: ")
        context = {**self.base_context, **{"signerPriv": signer_pkey}}
        self.run_method("authorizeValidatorSigner", context)

    def vote(self, vote_num: int = 0, validator: str = "") -> None:
        if vote_num == 0:
            vote_num = take_input(int, "Enter amount of MAP to vote with: ")
            validator = take_input(str, "Enter validator to vote for: ")
        context = {**self.base_context, **{"validator": validator, "voteNum": vote_num}}
        self.run_method("vote", context)

    def get_total_votes_for_eligible_validator(self) -> None:
        context = {"rpcaddr": self.rpcaddr, "rpcport": self.rpcport}
        self.run_method("getTotalVotesForEligibleValidators", context)
