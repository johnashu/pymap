from pymap.tools.utils import take_input
from getpass import getpass


class AtlasMethods:
    def __init__(self, **kw) -> None:
        super(AtlasMethods, self).__init__(**kw)

    def new_validator(self, datadir: str = "") -> None:
        if not datadir:
            datadir = take_input(str, "Enter Directory to save keystore: ")
            pw1, pw2 = "1", "2"
            while 1:
                pw1 = getpass(prompt="Enter Keystore password: ")
                pw2 = getpass(prompt="Re-Enter Keystore password: ")
                if pw1 != pw2:
                    print("Passwords do NOT match, Please try again!")
                else:
                    break

        args = ["account", "new"]
        context = {"datadir": datadir}
        self.run_method("", context, args=args, prog="atlas", std_in=f"{pw1}\n{pw2}\n")

    def join_network(
        self,
        datadir: str = "./node",
        port: int = 30321,
        miner_validator: str = "0x98efa292822eb7b3045c491e8ae4e82b3b1ac005",
        unlock: str = "0x98efa292822eb7b3045c491e8ae4e82b3b1ac005",
        syncmode: str = "full",
        password: str = ''
    ) -> None:
        if not datadir:
            datadir = take_input(str, "Enter Directory to save keystore: ")

        context = {
            "datadir": datadir,
            "syncmode": syncmode,
            "port": port,
            "mine": "",
            "miner.validator": miner_validator,
            "unlock": unlock,
        }
        self.run_method("", context, prog="atlas", std_in=f"{password}\n")


# ./atlas --datadir ./node --syncmode "full" --port 30321 --mine --miner.validator 0x98efa292822eb7b3045c491e8ae4e82b3b1ac005 --unlock 0x98efa292822eb7b3045c491e8ae4e82b3b1ac005
