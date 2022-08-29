from pymap.includes.config import envs, rpc_url
from pymap.interactive.interactive import InteractiveSetup
from pymap.methods.rpc_methods import RpcMethods

from_env = envs.__dict__
print(from_env)


def is_testnet(context) -> None:
    while 1:
        try:
            testnet = int(
                input(
                    "Please indicate if you wish to use Testnet or Mainnet\n\t* [1] Testnet\n\t* [2] Mainnet\n\t>>> "
                )
            )
            break
        except ValueError:
            pass
    if testnet == 1:
        context.update(
            {
                "rpcaddr": context["testnet"],
            }
        )
        return True, context
    return False, context


if __name__ == "__main__":

    address = "0xb4e1bc0856f70a55764fd6b3f8dd27f2162108e9"
    rpc = RpcMethods()
    res = rpc._get_validators(endpoint=rpc_url)
    print(res)

    balance = rpc.get_balance(address)
    print(balance)

    tn, context = is_testnet(from_env)

    i = InteractiveSetup(**context)
    i.start()
