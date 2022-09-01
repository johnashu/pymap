# from pymap.methods.marker_methods import MarkerMethods
from pymap.includes.config import envs, base_fields
from pymap.tools.utils import take_input, log


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


import sys
class HandleInput:

    def __init__(self, reset: int = 0, **kw):
        super(HandleInput, self).__init__()

    def f(self, context):
        
        context.update(self.handle_input(context))
        # locals()['tes'] = 'hello'
        print(locals())
        print(context)
        for k, v in context.items():
            print(k, v)
            print(k)
            locals()[k] = v
        del context, k, v
        print(locals())
        print(self.voteNum)

    def handle_input(self, context:dict) -> None:
        locals = {k:v for k, v in context.items() if not v}
        for k, v in locals.items():
            print(k, type(v))
            try:
                arg = eval(f'self.{k}')
            except AttributeError:
                arg = ''
            i = take_input(type(v), f"Please Enter {' '.join(k.split('_')).title()} ({arg}): ")
            print(arg, i)
            if not i:
                i = eval(f'self.{k}')
            else:
                exec(f'self.{k} = {i}')
            locals[k] = i
            print(locals)

        print(locals)   
        return locals

# m = InteractiveSetup(**from_env)
class MarkerMethods(RPC, PrintStuff, HandleInput):

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


# m = InteractiveSetup(**from_env)
# print(InteractiveSetup.mro())
# m.f()


# m = MarkerMethods(**base_fields)
# # h = HandleInput()
# m.f(some_other_stuff=100, signer_pkey='hello', validator='', voteNum=0)

isSigner = False
sp = '/signer/pass'
p = ''
d = '/default/pass'

passwordFile = sp if isSigner and sp else p if p and not isSigner else d
print(passwordFile)
