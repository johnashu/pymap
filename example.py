from audioop import add
from webbrowser import get
from pymap.methods.marker_methods import MarkerMethods
from pymap.includes.config import envs, base_fields, rpc_url
from pymap.interactive.interactive import InteractiveSetup
from pymap.methods.rpc_methods import RpcMethods

from_env = envs.__dict__
print(from_env)

if __name__ == "__main__":    

    address = '0xb4e1bc0856f70a55764fd6b3f8dd27f2162108e9'
    rpc = RpcMethods()
    res = rpc._get_validators(endpoint=rpc_url)
    print(res)

    balance = rpc.get_balance(address, endpoint=rpc_url)
    print(balance)

    i = InteractiveSetup(**from_env)
    i.start()
