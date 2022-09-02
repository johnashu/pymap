from pymap.tools.utils import is_signer
import logging as log


class AtlasAttachMethods:
    def __init__(self, **kw) -> None:
        super(AtlasAttachMethods, self).__init__(**kw)

    def prepare_attach(self, keystore: str) -> list:
        attach = "attach"
        ipc = f"{keystore.split('keystore')[0]}atlas.ipc"
        return [attach, ipc]

    def get_eth_block_number_from_node(
        self, context: dict = dict(keystore=str())
    ) -> None:
        isSigner = is_signer()
        context.update(self.handle_input(context), isSigner=isSigner)
        args = self.prepare_attach(context["keystore"])
        method = "eth.blockNumber"

        log.info(args)

        self.run_method("", context, args=args, prog="atlas", std_in=f"{method}\n")
