class MarkerMethods:
    def __init__(self, **kw) -> None:
        super(MarkerMethods, self).__init__(**kw)

    def create_account(self, context: dict = dict(name=str())) -> None:
        """
        https://docs.maplabs.io/develop/map-relay-chain/marker/aboutcommon#createaccount"""

        context.update(
            self.handle_input(
                {**self.base_context, **context},
            )
        )
        self.run_method("createAccount", context)

    # Locking, Unlocking & Withdrawal
    def locked_map(self, context: dict = dict(lockedNum=int())) -> None:
        context.update(self.handle_input({**self.base_context, **context}))
        self.run_method("lockedMAP", context)

    def unlock_map(self, context: dict = dict(mapValue=int())) -> None:
        context.update(self.handle_input({**self.base_context, **context}))
        self.run_method("unlockMap", context)

    def get_account_nonvoting_locked_gold(
        self, context: dict = dict(target=str())
    ) -> None:
        context.update(
            self.handle_input(
                {**self.base_context, **context}, remove=("password", "keystore")
            )
        )
        self.run_method("getAccountNonvotingLockedGold ", context)

    def get_account_total_locked_gold(self, context: dict = dict(target=str())) -> None:
        context.update(
            self.handle_input(
                {**self.base_context, **context}, remove=("password", "keystore")
            )
        )
        self.run_method("getAccountTotalLockedGold", context)

    def get_active_votes_for_validator_by_account(
        self, context: dict = dict(target=str())
    ) -> None:
        context.update(
            self.handle_input(
                {**self.base_context, **context}, remove=("password", "keystore")
            )
        )
        self.run_method("getActiveVotesForValidatorByAccount", context)

    def get_pending_withdrawals(self, context: dict = dict(target=str())) -> None:
        context.update(
            self.handle_input(
                {**self.base_context, **context}, remove=("password", "keystore")
            )
        )
        self.run_method("getPendingWithdrawals", context)

    def withdraw_map(self, context: dict = dict(withdrawIndex=int())) -> None:
        context.update(self.handle_input({**self.base_context, **context}))
        self.run_method("withdrawMap", context)

    # SIGNING AND REGISTERING
    def make_ECDSA_signature_from_signer(
        self, context: dict = dict(validator=str(), signerPriv=str())
    ) -> None:
        context.update(
            self.handle_input(
                {**self.base_context, **context}, remove=("password", "keystore")
            )
        )
        self.run_method("makeECDSASignatureFromSigner", context, isECDSA=True)

    # Deprecated for generateSignerProof
    # def make_BLS_proof_of_possession_from_signer(
    #     self, context: dict = dict(validator=str(), signerPriv=str())
    # ) -> None:
    #     context.update(
    #         self.handle_input(
    #             {**self.base_context, **context},
    #             remove=("password", "keystore")
    #         )
    #     )
    #     self.run_method("MakeBLSProofOfPossessionFromSigner", context)

    def generate_signer_proof(
        self, context: dict = dict(validator=str(), signerPriv=str())
    ) -> None:
        context.update(
            self.handle_input(
                {**self.base_context, **context}, remove=("password", "keystore")
            )
        )
        self.run_method("generateSignerProof ", context)

    def authorise_validator_signer_by_signature(
        self, context: dict = dict(signer=str(), signature=str())
    ) -> None:
        context.update(self.handle_input({**self.base_context, **context}))
        self.run_method("authorizeValidatorSignerBySignature  ", context)

    def authorise_validator_signer(
        self, context: dict = dict(signerPriv=str())
    ) -> None:
        context.update(self.handle_input({**self.base_context, **context}))
        self.run_method("authorizeValidatorSigner", context)

    def register(
        self, context: dict = dict(commission=int(), signerPriv=str())
    ) -> None:
        context.update(self.handle_input({**self.base_context, **context}))
        c = context["commission"]
        context["commission"] = str(int(c) * 10000)
        self.run_method("register", context)

    def deregister(self):
        self.run_method("deregister", self.base_context)

    def revert_register(self):
        """cancel deregister"""
        self.run_method("revertRegister", self.base_context)

    # VOTING

    def vote(
        self, context: dict = dict(voteNum=int(), signerPriv=str(), validator=str())
    ) -> None:
        context.update(self.handle_input({**self.base_context, **context}))
        self.run_method("vote", context)

    def activate_votes(self, context: dict = dict(validator=str())) -> None:
        context.update(self.handle_input({**self.base_context, **context}))
        self.run_method("activate", context)

    def revoke_pending_votes(
        self, context: dict = dict(mapValue=int(), validator=str())
    ) -> None:
        context.update(self.handle_input({**self.base_context, **context}))
        self.run_method("revokePending", context)

    def revoke_active_votes(
        self, context: dict = dict(mapValue=int(), validator=str())
    ) -> None:
        context.update(self.handle_input({**self.base_context, **context}))
        self.run_method("revokeActive", context)

    def get_total_votes_for_eligible_validator(self) -> None:
        context = {"rpcaddr": self.rpcaddr}
        if self.rpcport:
            context.update({"rpcport": self.rpcport})
        self.run_method("getTotalVotesForEligibleValidators", context)

    def get_validator_reward_info(self) -> None:
        context = {"rpcaddr": self.rpcaddr}
        if self.rpcport:
            context.update({"rpcport": self.rpcport})
        self.run_method("getValidatorRewardInfo", context)

    # TX and things
    def transfer(self, context: dict = dict(target=str(), amount=int())) -> None:
        context.update(self.handle_input({**self.base_context, **context}))
        self.run_method("transfer", context)

    # Validator info
    def get_validator(self, context: dict = dict(validator=str())) -> None:
        context.update(
            self.handle_input(
                {**self.base_context, **context}, remove=("password", "keystore")
            )
        )
        self.run_method("getValidator", context)
