from pymap.tools.file_op import save_file
import logging as log


def create_systemd(
    context: dict = {
        "working_dir": str(),
        "binary": str(),
        "password": str(),
        "datadir": str(),
        "miner.validator": str(),
        "unlock": str(),
        "testnet": str(),
    },
    serviceName: str = "atlasNode",
    template: dict = {},
) -> None:

    sysd = template.format(*[x for x in context.values()])
    print(sysd)
    save_file(f"/etc/systemd/system/{serviceName}.service", sysd)
    return sysd
