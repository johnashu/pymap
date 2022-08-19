from pymap.process.process_command import RunProcess
from pymap.interactive.display import PrintStuff
from pymap.methods.altas_methods import AtlasMethods
from pymap.tools.utils import take_input


class MarkerMethods(RunProcess, PrintStuff, AtlasMethods):

    base_fields = ("rpcaddr", "rpcport", "keystore", "password")

    def __init__(self, **base_fields: dict) -> None:
        self.set_fields(**base_fields)
        self.base_context = {
            k: v for k, v in base_fields.items() if k in self.base_fields and v
        }
        print(self.base_context)
        super(MarkerMethods, self).__init__(**base_fields)

    def set_fields(self, **base_fields) -> None:
        for k, v in base_fields.items():
            setattr(self, k, str(v))

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

    def register(self, commission: int = 0, signer_pkey: str = "") -> None:
        if not signer_pkey:
            signer_pkey = take_input(str, "Enter Signer Private Key: ")
        if not commission:
            # TODO: allow float input -> convert to Wei.
            commission = take_input(int, "Enter Commission of validator")
        context = {
            **self.base_context,
            **{"signerPriv": signer_pkey, "commission": commission},
        }
        self.run_method("register", context)

    def deregister(self):
        self.run_method("deregister", self.base_context)

    def revert_register(self):
        """cancel deregister"""
        self.run_method("revertRegister", self.base_context)

    def vote(self, vote_num: int = 0, validator: str = "") -> None:
        if vote_num == 0:
            vote_num = take_input(int, "Enter amount of MAP to vote with: ")
        if not validator:
            validator = take_input(str, "Enter validator to vote for: ")
        context = {**self.base_context, **{"validator": validator, "voteNum": vote_num}}
        self.run_method("vote", context)

    def activate_votes(self, validator: str = "") -> None:
        if not validator:
            validator = take_input(str, "Enter validator to activate votes for: ")
        context = {**self.base_context, **{"validator": validator}}
        self.run_method("activate", context)

    def revoke_pending_votes(self, validator: str = "", amount: int = 0) -> None:
        if amount == 0:
            amount = take_input(int, "Enter amount of votes to revoke: ")
        if not validator:
            validator = take_input(str, "Enter validator to activate votes for: ")
        context = {**self.base_context, **{"validator": validator, "mapValue": amount}}
        self.run_method("revokePending", context)

    def revoke_active_votes(self, validator: str = "", amount: int = 0) -> None:
        if amount == 0:
            amount = take_input(int, "Enter amount of votes to revoke: ")
        if not validator:
            validator = take_input(str, "Enter validator to activate votes for: ")
        context = {**self.base_context, **{"validator": validator, "mapValue": amount}}
        self.run_method("revokeActive", context)

    def get_total_votes_for_eligible_validator(self) -> None:
        context = {"rpcaddr": self.rpcaddr}
        if self.rpcport:
            context.update({"rpcport": self.rpcport})
        self.run_method("getTotalVotesForEligibleValidators", context)

    def make_ECDSA_signature_from_signer(
        self, validator: str = 0, signer_pkey: str = ""
    ) -> None:
        if not signer_pkey:
            signer_pkey = take_input(str, "Enter Signer Private Key: ")
        if not validator:
            validator = take_input(str, "Enter validator")
        context = {
            **self.base_context,
            **{"signerPriv": signer_pkey, "validator": validator},
        }
        self.run_method("makeECDSASignatureFromSigner", context)

    def make_BLS_proof_of_possession_from_signer(
        self, validator: str = 0, signer_pkey: str = ""
    ) -> None:
        if not signer_pkey:
            signer_pkey = take_input(str, "Enter Signer Private Key: ")
        if not validator:
            validator = take_input(str, "Enter validator")
        context = {
            **self.base_context,
            **{"signerPriv": signer_pkey, "validator": validator},
        }
        self.run_method("MakeBLSProofOfPossessionFromSigner", context)
