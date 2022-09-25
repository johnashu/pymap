from pymap.includes.setup._envs import Envs
from pymap.includes.setup._logging import start_logger
from pymap.includes.setup._paths import *
import sys

sys.dont_write_bytecode = True

verbose = False

envs = Envs()
alert_envs = Envs(envFile="alerts.env")
log = start_logger(verbose=verbose)

version = "1.0.0"

server_hostname = ""

api_data_fn = "api_data"

marker = "marker"
atlas = "atlas"

base_fields = {
    "rpcaddr": "",
    "rpcport": 0,
    "keystore": "",
    "password": "",
    "name": "",
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
makalu_api_url = "https://makalu-api.mapscan.io/scan/"

_rpc_endpoint = rpc_url
_timeout = 30
