from pymap.rpc.request import RpcRequest, _default_endpoint, _default_timeout
from pymap.rpc.exceptions import (
    TxConfirmationTimedoutError,
    InvalidRPCReplyError,
)


class RpcMethods(RpcRequest):
    def __init__(self) -> None:
        pass

    def get_validators(
        self,
        endpoint=_default_endpoint,
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
                method, params=params, endpoint=endpoint, timeout=timeout
            )["result"]
        except KeyError as e:
            raise InvalidRPCReplyError(method, endpoint) from e