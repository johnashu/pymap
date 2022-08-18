from webbrowser import get
from pymap.methods.marker_methods import MarkerMethods
from pymap.includes.config import envs, base_fields, rpc_url
from pymap.interactive.interactive import InteractiveSetup
from pymap.methods.rpc_methods import RpcMethods

from_env = envs.__dict__
print(from_env)

if __name__ == "__main__":
    # m = MarkerMethods(**from_env)
    i = InteractiveSetup(**from_env)
    # i.start()'

    rpc = RpcMethods()
    res = rpc.get_validators(endpoint=rpc_url)
    print(res)
