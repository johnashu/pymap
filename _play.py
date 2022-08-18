# from pymap.methods.marker_methods import MarkerMethods
from pymap.includes.config import envs, base_fields


from_env = envs.__dict__
print(from_env)


# m.new_validator(datadir="test")
# m.create_account()
# m.get_total_votes_for_eligible_validator()


class RPC:
    pass


class PrintStuff:
    def __init__(self, reset: int = 0, **kw):
        self.reset = reset
        self.print_stars = "*" * 93
        super(PrintStuff, self).__init__()


class MarkerMethods(RPC, PrintStuff):

    base_fields = ("rpcaddr", "rpcport", "keystore", "password")

    def __init__(self, **base_fields: dict) -> None:
        self.set_fields(**base_fields)
        self.base_context = {
            k: v for k, v in base_fields.items() if k in self.base_fields
        }
        print(self.rpcaddr)
        super(MarkerMethods, self).__init__(**base_fields)

    def set_fields(self, **base_fields) -> None:
        for k, v in base_fields.items():
            setattr(self, k, str(v))


class Menu(MarkerMethods):
    def __init__(self, **base_fields: dict) -> None:
        # super().__init__(**base_fields)
        super(Menu, self).__init__(**base_fields)


class InteractiveSetup(Menu):
    def __init__(self, **base_fields: dict) -> None:
        # super().__init__(**base_fields)
        super(InteractiveSetup, self).__init__(**base_fields)

    def f(self):
        print(self.print_stars)


m = InteractiveSetup(**from_env)
print(InteractiveSetup.mro())
m.f()
