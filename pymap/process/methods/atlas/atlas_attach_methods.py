from pymap.tools.utils import log, readable_price
import inspect


class AtlasAttachMethods:
    """Class method names are named using the attach method but swapping . for _
    handle_attach will convert the class method name to the attach method name
    """

    local_block = 0

    def __init__(self, **kw) -> None:
        super(AtlasAttachMethods, self).__init__(**kw)

    def handle_attach(self, context: dict, msg: str, localBlock: bool = False) -> None:
        method = inspect.stack()[1][3].replace("_", ".")
        attach = "attach"
        keystore = context.get("keystore")
        if not keystore:
            log.error(f"No Keystore Found!")
            return
        ipc = f"{keystore.split('keystore')[0]}atlas.ipc"
        args = [attach, ipc]
        self.run_method(
            "",
            context,
            args=args,
            prog="atlas",
            std_in=f"{method}\n",
            isAttach=True,
            prefix=msg + f"for {args[-1]}",
            localBlock=localBlock,
        )

    def admin_peers_length(self, context: dict = dict(keystore=str())) -> None:
        context.update(self.handle_input(context))
        msg = f"Number of connected Peers "
        self.handle_attach(context, msg)

    def eth_blockNumber(self, context: dict = dict(keystore=str())) -> None:
        context.update(self.handle_input(context))
        msg = f"Block Number "
        self.handle_attach(context, msg, localBlock=True)
