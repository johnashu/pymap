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
            if not pw2:
                continue
            if pw1 != pw2:
                print("Passwords do NOT match, Please try again!")
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
        self.run_method("", context, prog="atlas", scrolling=True)

    def setup_atlas_node_service(
        self,
        context: dict = dict(
            working_dir=str(),
            binaries=str(),
            passwordFile=str(),
            datadir=str(),
            validator=str(),
            unlock=str(),
        ),
    ) -> None:
        context.update(self.handle_input(context))
        create_systemd(context)

        commands = (
            "sudo mv atlasNode.service /etc/systemd/system/atlasNode.service",
            "sudo service atlasNode stop",
            "sudo systemctl daemon-reload ",
            "sudo chmod 644 /etc/systemd/system/atlasNode.service",
            "sudo systemctl enable atlasNode.service",
            "sudo service atlasNode start",
        )

        for cmd in commands:
            self.run_method(
                cmd.split(),
                {},
                prog="",
            )

    def show_tail(self) -> None:
        cmd = "tail -f /var/log/syslog"
        self.run_method(cmd.split(), {}, prog="", scrolling=True)
