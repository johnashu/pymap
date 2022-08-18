import requests


class RPCError(RuntimeError):
    """
    Exception raised when RPC call returns an error
    """

    def __init__(self, method, endpoint, error):
        self.error = error
        super().__init__(f"Error in reply from {endpoint}: {method} returned {error}\n")


class RequestsError(requests.exceptions.RequestException):
    """
    Wrapper for requests lib exceptions
    """

    def __init__(self, endpoint):
        super().__init__(f"Error connecting to {endpoint}")


class RequestsTimeoutError(requests.exceptions.Timeout):
    """
    Wrapper for requests lib Timeout exceptions
    """

    def __init__(self, endpoint):
        super().__init__(f"Error connecting to {endpoint}")


class InvalidRPCReplyError(RuntimeError):
    """
    Exception raised when RPC call returns unexpected result
    Generally indicates SUI API has been updated & suihmy library needs to be updated as well
    """

    def __init__(self, method, endpoint):
        super().__init__(f"Unexpected reply for {method} from {endpoint}")


class TxConfirmationTimedoutError(AssertionError):
    """
    Exception raised when a transaction is sent to the chain
    But not confirmed during the timeout period specified
    """

    def __init__(self, msg):
        super().__init__(f"{msg}")
