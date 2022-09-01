import os
from getpass import getpass
from pymap.tools.file_op import save_file
from pymap.tools.create_service import create_systemd
from pymap.tools.utils import is_signer
from pymap.tools.key_from_keystore import pk_from_store


class AtlasMethods:
    def __init__(self, **kw) -> None:
        super(AtlasMethods, self).__init__(**kw)

    def new_account(self, context: dict = dict(datadir=str())) -> None:
        context.update(self.handle_input(context))
        pw1, pw2 = "1", "2"
        isSigner = is_signer()

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
            isSigner=isSigner,
        )

        passwordFile = self.signer_passwordFile if isSigner else self.passwordFile
        default_pw_fn = "signer_password" if isSigner else 'password'

        save_file(
            passwordFile if passwordFile else os.path.join(os.getcwd(), default_pw_fn),
            pw1,
        )

        if isSigner:
            self.signer_password = pw1
            self.signer_address, self.signerPriv = pk_from_store(
                self.signer_keystore, self.signer_password
            )
            self.unlock = self.signer_address
            self.__dict__["miner.validator"] = self.signer_address
            self.update_env(self.base_field_keys)

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
        context: dict = {
            "working_dir": str(),
            "binaries": str(),
            "passwordFile": str(),
            "datadir": str(),
            "miner.validator": str(),
            "unlock": str(),
        },
    ) -> None:
        context.update(
            self.handle_input(context), isSigner=True, signer_fields=("passwordFile")
        )
        if self.testnet == self.rpcaddr:
            context["testnet"] = "--testnet"
        create_systemd(context)

        commands = (
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
