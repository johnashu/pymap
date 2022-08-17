from pymap.process.process_command import RunProcess


class Methods(RunProcess):

    base_fields = ("rpcaddr", "rpcport", "keystore", "password")

    def __init__(self, **base_fields: dict) -> None:
        self.set_fields(**base_fields)
        self.base_context = {
            k: v for k, v in base_fields.items() if k in self.base_fields
        }

    def set_fields(self, **base_fields) -> None:
        for k, v in base_fields.items():
            setattr(self, k, str(v))

    def new_validator(self, datadir: str = "") -> None:
        args = ["account", "new"]
        context = {"datadir": datadir}
        self.run_method("", context, args=args, prog="atlas")

    def create_account(self) -> None:
        """
        https://docs.maplabs.io/develop/map-relay-chain/marker/aboutcommon#createaccount
        """

        context = {**self.base_context, **{"namePrefix": "validator"}}
        self.run_method("createAccount", context)

    def locked_map(self, locked_num: int) -> None:
        # Lock MAP in Validator - Stake

        context = {**self.base_context, **{"lockedNum": locked_num}}
        self.run_method("lockedMAP", context)

    def authorise_validator_signer(self, signer_pkey: int) -> None:
        context = {**self.base_context, **{"signerPriv": signer_pkey}}
        self.run_method("authorizeValidatorSigner", context)

    def vote(self, vote_num: int, validator: str) -> None:
        context = {**self.base_context, **{"validator": validator}}
        self.run_method("vote", context)

    def get_total_votes_for_eligible_validator(self) -> None:
        context = {"rpcaddr": self.rpcaddr, "rpcport": self.rpcport}
        self.run_method("getTotalVotesForEligibleValidators", context)