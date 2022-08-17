from pymap.process.process_command import RunProcess


class Methods(RunProcess):
    def __init__(self, **base_fields: dict) -> None:
        self.set_fields(**base_fields)
        self.base_context = base_fields

    def set_fields(self, **base_fields) -> None:
        for k, v in base_fields.items():
            setattr(self, k, str(v))

    def create_account(self) -> None:
        # Create account

        context = {**self.base_context, **{"namePrefix": "validator"}}
        self.run_method("createAccount", context)

    def locked_map(self, locked_num: int) -> None:
        # Lock MAP in Validator - Stake

        context = {**self.base_context, **{"lockedNum": locked_num}}
        self.run_method("lockedMAP", context)

    def authorise_validator_signer(self, signer_pkey: int) -> None:
        context = {**self.base_context, **{"signerPriv": signer_pkey}}
        self.run_method("authorizeValidatorSigner", context)
