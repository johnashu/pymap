from pymap.includes.config import envs, rpc_url
from pymap.interactive.interactive import InteractiveSetup
from pymap.methods.rpc_methods import RpcMethods

from pymap.tools.create_service import create_systemd

from_env = envs.__dict__
print(from_env)

if __name__ == "__main__":

    address = "0x3E8dF1A18E97fAA3235EA731A5C7B7C2455D21E8"
    rpc = RpcMethods(**{"rpcarddr": rpc_url})
    res = rpc._get_validators()
    print(res)

    balance = rpc.get_balance(address)
    print(balance)

    # create_systemd()
    i = InteractiveSetup(**from_env)
    i.get_balance(address)
    v = i._get_validators()
    tx = i.rpc_request(
        "eth_getTransactionByHash",
        ["0x55e46782f48bbd36def69f5624d073ed5ff4c15e7da4300bc0effc297c59820c"],
        endpoint="http://18.142.54.137:7445",
    )
    print(tx)
    print(v)
    # i.start()
