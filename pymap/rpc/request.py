import json
import requests
import curlify

from .exceptions import RequestsError, RequestsTimeoutError, RPCError

from pymap.includes.config import rpc_url, makalu_api_url, staking_graph_url


class RpcRequest:

    _rpc_endpoint = rpc_url
    _makalu_api_url = makalu_api_url
    _staking_graph_url = staking_graph_url
    _timeout = 30

    def base_request(
        self,
        method,
        params=None,
        endpoint=None,
        timeout=None,
        call_type="POST",
        graph: bool = False,
    ) -> str:
        """
        Basic RPC request

        Parameters
        ---------
        method: str
            RPC Method to call
        params: :obj:`list`, optional
            Parameters for the RPC method
        endpoint: :obj:`str`, optional
            Endpoint to send request to
        timeout: :obj:`int`, optional
            Timeout in seconds

        Returns
        -------
        str
            Raw output from the request

        Raises
        ------
        TypeError
            If params is not a list or None
        RequestsTimeoutError
            If request timed out
        RequestsError
            If other request error occured
        """
        headers = {"Content-Type": "application/json"}
        kw = dict(
            headers=headers,
            timeout=timeout,
            allow_redirects=True,
        )
        params = self.handle_request_type(
            list if call_type == "POST" and not graph else dict, params
        )
        try:

            if call_type == "POST":
                if not graph:
                    payload = {
                        "id": "1",
                        "jsonrpc": "2.0",
                        "method": method,
                        "params": params,
                    }
                else:
                    payload = params
                kw["data"] = json.dumps(payload, indent=4)

            elif call_type == "GET":
                kw["params"] = params
                endpoint = f"{endpoint}{method}"

            resp = requests.request(call_type, endpoint, **kw)

            self.star_surround(curlify.to_curl(resp.request))
            return resp.content
        except requests.exceptions.Timeout as err:
            raise RequestsTimeoutError(endpoint) from err
        except requests.exceptions.RequestException as err:
            raise RequestsError(endpoint) from err

    def rpc_request(
        self,
        method,
        params=None,
        endpoint=None,
        timeout=None,
        call_type: str = "POST",
        graph: bool = False,
    ) -> dict:
        """
        RPC request

        Parameters
        ---------
        method: str
            RPC Method to call
        params: :obj:`list`, optional
            Parameters for the RPC method
        endpoint: :obj:`str`, optional
            Endpoint to send request to
        timeout: :obj:`int`, optional
            Timeout in seconds

        Returns
        -------
        dict
            Returns dictionary representation of RPC response
            Example format:
            {
                "jsonrpc": "2.0",
                "id": 1,
                "result": ...
            }

        Raises
        ------
        RPCError
            If RPC response returned a blockchain error

        See Also
        --------
        base_request
        """
        raw_resp = self.base_request(
            method, params, endpoint, timeout, call_type, graph
        )

        try:
            resp = json.loads(raw_resp)
            if "error" in resp:
                raise RPCError(method, endpoint, str(resp["error"]))
            return resp
        except json.decoder.JSONDecodeError as err:
            raise RPCError(method, endpoint, raw_resp) from err

    def handle_request_type(self, obj: object, params: list) -> object:
        if not params:
            params = obj()
        elif not isinstance(params, obj):
            raise TypeError(f"invalid type {params.__class__}")
        return params
