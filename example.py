from audioop import add
from webbrowser import get
from pymap.methods.marker_methods import MarkerMethods
from pymap.includes.config import envs, base_fields, rpc_url
from pymap.interactive.interactive import InteractiveSetup
from pymap.methods.rpc_methods import RpcMethods

from_env = envs.__dict__
print(from_env)

if __name__ == "__main__":
    m = MarkerMethods(**from_env)
    print(dir(MarkerMethods))
    i = InteractiveSetup(**from_env)
    i.start()

    # address = '0xb4e1bc0856f70a55764fd6b3f8dd27f2162108e9'
    # rpc = RpcMethods()
    # res = rpc.get_validators(endpoint=rpc_url)
    # print(res)

    # balance = rpc.get_balance(address, endpoint=rpc_url)
    # print(balance)
    import itertools
    from types import FunctionType

    def listMethods(cls):
        return set(
            x
            for x, y in cls.__dict__.items()
            if isinstance(y, (FunctionType, classmethod, staticmethod))
        )

    def listParentMethods(cls):
        return set(
            itertools.chain.from_iterable(
                listMethods(c).union(listParentMethods(c)) for c in cls.__bases__
            )
        )

    def list_subclass_methods(cls, is_narrow):
        methods = listMethods(cls)
        if is_narrow:
            parentMethods = listParentMethods(cls)
            return set(cls for cls in methods if not (cls in parentMethods))
        else:
            return methods

    print(list_subclass_methods(MarkerMethods, True))
