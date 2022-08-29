import os
from getpass import getpass
from pymap.tools.file_op import save_file
from pymap.tools.create_service import create_systemd


class AtlasMethods:
    def __init__(self, **kw) -> None:
        super(AtlasMethods, self).__init__(**kw)

    def new_validator(self, context: dict = dict(datadir=str())) -> None:
        context.update(self.handle_input(context))
        pw1, pw2 = "1", "2"
        while 1:
            pw1 = getpass(prompt="Enter Keystore password: ")
            if not pw1:
                continue
            pw2 = getpass(prompt="Re-Enter Keystore password: ")
            if pw1 != pw2:
                print("Passwords do NOT match, Please try again!")
            if not pw2:
                continue
            else:
                break

        args = ["account", "new"]
        self.run_method(
            "",
            context,
            args=args,
            prog="atlas",
            std_in=f"{pw1}\n{pw2}\n",
            save_keystore=True,
        )
        to_write = pw1
        save_file(
            self.passwordFile
            if self.passwordFile
            else os.path.join(os.getcwd(), "password"),
            to_write,
        )

    def join_network(
        self,
        context: dict = {
            "datadir": str(),
            "syncmode": str(),
            "port": int(),
            "miner.validator": str(),
            "unlock": str(),
        },
    ) -> None:
        context.update(self.handle_input(context))
        context.update({"mine": ""})
        self.run_method("", context, prog="atlas")

    def setup_atlas_node_service(
        self,
        context: dict = dict(
            working_dir=str(),
            binaries=str(),
            password=str(),
            datadir=str(),
            validator=str(),
            unlock=str(),
        ),
    ) -> None:
        context.update(self.handle_input(context))
        create_systemd(context)
        self.run_method(
            ["mv", "atlasNode.service", "/etc/systemd/system/atlasNode.service"],
            {},
            prog="",
        )

        script = os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    "..",
                    "scripts",
                    "startNode.sh",
                )

        self.run_method(
            [
                "bash",
                script,
            ],
            {},
            prog="",
        )
