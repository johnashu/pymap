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

