from pymap.includes.setup._envs import Envs
from pymap.includes.setup._logging import start_logger
from pymap.includes.setup._paths import *
import sys

sys.dont_write_bytecode = True

verbose = False

envs = Envs()
log = start_logger(verbose=verbose)

version = "1.0.0"

api_data_fn = "api_data"

marker = "marker"
atlas = "atlas"

base_fields = {
    "rpcaddr": "",
    "rpcport": 0,
    "keystore": "",
    "password": "",
    "namePrefix": "",
    "lockedNum": 0,
    "signerPriv": "",
    "validator": "",
    "voteNum": 0,
}

ignore = ("binaries",)
# main_menu = os.path.join(
#     os.path.dirname(os.path.abspath(__file__)), "messages", "fullmenu.txt"
# )

rpc_url = "https://poc3-rpc.maplabs.io"

_default_endpoint = rpc_url
_default_timeout = 30
