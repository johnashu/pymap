from pymap.rpc.request import RpcRequest, _default_endpoint, _default_timeout
from pymap.rpc.exceptions import (
    TxConfirmationTimedoutError,
    InvalidRPCReplyError,
)
from pymap.tools.utils import take_input, log


class RpcMethods(RpcRequest):
    def __init__(self, **kw) -> None:
        super(RpcMethods, self).__init__(**kw)

    def _get_validators(
        self,
        # endpoint=_default_endpoint,
        timeout=_default_timeout,
    ) -> list:
        """
        Determine whether we are selected as validators who can participate in block generation

        Parameters
        ----------
        endpoint: :obj:`str`, optional
            Endpoint to send request to
        timeout: :obj:`int`, optional
            Timeout in seconds

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
        params = []
        try:
            return self.rpc_request(
                method, params=params, endpoint=self.rpcaddr, timeout=timeout
            )["result"]
        except KeyError as e:
            raise InvalidRPCReplyError(method, self.rpcaddr) from e

    def _get_balance(
        self,
        address: str,
        block: str = "latest",
        # endpoint=_default_endpoint,
        timeout=_default_timeout,
    ) -> list:
        """
        Check Balance of address

        Parameters
        ----------
        address: :obj: str
            Address to check
        endpoint: :obj:`str`, optional
            Endpoint to send request to
        timeout: :obj:`int`, optional
            Timeout in seconds

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
                    method, params=params, endpoint=self.rpcaddr, timeout=timeout
                )["result"],
                16,
            )
        except KeyError as e:
            raise InvalidRPCReplyError(method, self.rpcaddr) from e

    def get_balance(self, address: str = "") -> int:
        if not address:
            address = self.handle_input({"default_address": self.default_address})[
                "default_address"
            ]
            # take_input(str, "Enter address to check: ")
        balance = self._get_balance(address)
        log.info(f"Balance of Address  {address}  ::  {balance}  MAP")
        return balance

    def check_if_selected(self, validator: str = "") -> bool:
        if not validator:
            validator = self.handle_input({"validator": self.validator})["validator"]

            # validator = take_input(
            #     str, "Enter validator address to check election status: "
            # )
        elected = self._get_validators()
        if validator in elected:
            log.info(f"Validator {validator} is Elected!!")
            return True
        log.info(f"Validator {validator} is NOT elected.")
        return False
