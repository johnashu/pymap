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

prog = "marker"

base_fields = {
    "rpcaddr": "127.0.0.1",
    "rpcport": 7445,
    "keystore": "/Users/alex/data/atlas-1/keystore/UTC--2022-06-14T05-46-17.312327000Z--73bc690093b9dd0400c91886184a60cc127b2c33",
    "password": "password",
    "namePrefix": "validator",
    "lockedNum": 1000000,
    "signerPriv": "0x",
    "validator": "0x",
    "voteNum": 10000,
}
