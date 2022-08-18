from pymap.tools.utils import take_input
from getpass import getpass


class AtlasMethods:
    def __init__(self, **kw) -> None:
        super(AtlasMethods, self).__init__(**kw)

    def set_fields(self, **base_fields) -> None:
        for k, v in base_fields.items():
            setattr(self, k, str(v))

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
