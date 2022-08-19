from pymap.tools.utils import take_input
from getpass import getpass


class AtlasMethods:
    def __init__(self, **kw) -> None:
        super(AtlasMethods, self).__init__(**kw)

    def new_validator(self, context: dict = dict(datadir = str())) -> None:
        context.update(self.handle_input(context))
        pw1, pw2 = "1", "2"
        while 1:
            pw1 = getpass(prompt="Enter Keystore password: ")
            pw2 = getpass(prompt="Re-Enter Keystore password: ")
            if pw1 != pw2:
                print("Passwords do NOT match, Please try again!")
            else:
                break

        args = ["account", "new"]
        self.run_method("", context, args=args, prog="atlas", std_in=f"{pw1}\n{pw2}\n")

def join_network(
        self,
        context: dict ={
            "datadir": str(),
            "syncmode": str(),
            "port": int(),
            "miner.validator": str(),
            "unlock": str(),
        }
    ) -> None:
        context.update(self.handle_input(context))
        context.update({'mine': ''})

        # context = {
        #     "datadir": datadir,
        #     "syncmode": syncmode,
        #     "port": port,
        #     "mine": "",
        #     "miner.validator": miner_validator,
        #     "unlock": unlock,
        # }
        self.run_method("", context, prog="atlas", shell=True)
