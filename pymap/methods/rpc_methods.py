from os import read
from pymap.rpc.request import RpcRequest
from pymap.rpc.exceptions import (
    TxConfirmationTimedoutError,
    InvalidRPCReplyError,
)
from pymap.tools.utils import log, readable_price


class RpcMethods(RpcRequest):
    def __init__(self, **kw) -> None:
        super(RpcMethods, self).__init__(**kw)

    def _get_block_number(
        self,
    ) -> list:
        """
        Get the current block number.

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

        method = "eth_blockNumber"
        try:
            return self.rpc_request(
                method, endpoint=self._rpc_endpoint, timeout=self._timeout
            )["result"]
        except KeyError as e:
            raise InvalidRPCReplyError(method, self._rpc_endpoint) from e

    def _get_validators(
        self,
    ) -> list:
        """
        Determine whether we are selected as validators who can participate in block generation

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

        method = "istanbul_getValidators"
        try:
            return self.rpc_request(
                method, endpoint=self._rpc_endpoint, timeout=self._timeout
            )["result"]
        except KeyError as e:
            raise InvalidRPCReplyError(method, self._rpc_endpoint) from e

    def _get_balance(
        self,
        address: str,
        block: str = "latest",
    ) -> list:
        """
        Check Balance of address

        Parameters
        ----------
        address: :obj: str
            Address to check

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

        method = "eth_getBalance"
        params = [address, block]
        try:
            return int(
                self.rpc_request(
                    method,
                    params=params,
                    endpoint=self._rpc_endpoint,
                    timeout=self._timeout,
                )["result"],
                16,
            )
        except KeyError as e:
            raise InvalidRPCReplyError(method, self._rpc_endpoint) from e

    def get_block_number(self) -> int:
        block = int(self._get_block_number(), 16)
        print(
            f"Current Block Number of {self._rpc_endpoint}  ::  [ {readable_price(block, d=0, show_decimals=False)} ]"
        )
        return block

    def get_balance(self, address: str = "") -> int:
        if not address:
            address = self.handle_input({"default_address": self.default_address})[
                "default_address"
            ]
        balance = self._get_balance(address)
        # log readable but return int.
        print(f"Balance of Address  {address}  ::  {readable_price(balance)}  MAP")
        return balance

    def check_if_selected(self, validator: str = "") -> bool:
        if not validator:
            validator = self.handle_input({"validator": self.signer})["validator"]

        elected = self._get_validators()
        if validator in elected:
            print(f"Validator {validator} is Elected!!")
            return True
        print(f"Validator {validator} is NOT elected.")
        return False
