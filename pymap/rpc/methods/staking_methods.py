from pymap.rpc.request import RpcRequest
from pymap.rpc.exceptions import (
    TxConfirmationTimedoutError,
    InvalidRPCReplyError,
)


class StakingGraph(RpcRequest):
    def __init__(self, **kw) -> None:
        super(StakingGraph, self).__init__(**kw)

    def _get_staking_validators(self) -> list:

        """
        Get the current staking validators.

        Returns
        -------
        Json Response

        Raises
        ------
        InvalidRPCReplyError
            If received unknown result from endpoint

        API Reference
        -------------

        """

        params = {
            "operationName": "validators",
            "variables": {},
            "query": "query validators {\n  allValidators {\n    validator\n    name\n    proportion\n    apy\n    totalVoteNum\n    commission\n    __typename\n  }\n}",
        }
        try:
            return self.rpc_request(
                "",
                params=params,
                endpoint=self._staking_graph_url,
                timeout=self._timeout,
                call_type="POST",
                graph=True,
            )["data"]["allValidators"]
        except KeyError as e:
            raise InvalidRPCReplyError("allValidators", self._staking_graph_url) from e

    def get_apy(self, address: str) -> float:
        if not address:
            vals = self.handle_input({"default_address": self.default_address})
            address = vals.get("default_address")
        try:
            validators = self._get_staking_validators()
            for x in validators:
                if x.get("validator") == address:
                    return x.get("apy")
        except:
            ...

        return 0
