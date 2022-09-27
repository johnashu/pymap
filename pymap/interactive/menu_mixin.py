from pymap.tools.methods_base import MethodsBase
from pymap.interactive.display import PrintStuff
from pymap.process.methods.atlas.altas_methods import AtlasMethods
from pymap.process.methods.atlas.atlas_attach_methods import AtlasAttachMethods
from pymap.rpc.methods.makalu_api_methods import MakaluApiMethods
from pymap.rpc.methods.rpc_methods import RpcMethods
from pymap.rpc.methods.staking_methods import StakingGraph
from pymap.process.process_command import RunProcess
from pymap.tools.handle_input import HandleInput
from pymap.process.methods.marker.marker_methods import MarkerMethods


class MenuMixin(
    MethodsBase,
    MarkerMethods,
    RunProcess,
    PrintStuff,
    AtlasMethods,
    AtlasAttachMethods,
    RpcMethods,
    MakaluApiMethods,
    StakingGraph,
    HandleInput,
):
    def __init__(self, **kw) -> None:
        super(MenuMixin, self).__init__(**kw)
