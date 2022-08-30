from pymap.includes.config import envs, rpc_url
from pymap.interactive.interactive import InteractiveSetup
from pymap.methods.rpc_methods import RpcMethods

from pymap.tools.create_service import create_systemd

from_env = envs.__dict__
print(from_env)

if __name__ == "__main__":

    address = "0xb4e1bc0856f70a55764fd6b3f8dd27f2162108e9"
    rpc = RpcMethods()
    res = rpc._get_validators(endpoint=rpc_url)
    print(res)

    balance = rpc.get_balance(address)
    print(balance)

    create_systemd()
    i = InteractiveSetup(**from_env)
    i.start()
