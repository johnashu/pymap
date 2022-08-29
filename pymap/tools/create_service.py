from pymap.tools.file_op import save_file
import logging as log


def create_systemd(
    context: dict = dict(
        working_dir="",
        binary="",
        password="",
        datadir="",
        validator="",
        unlock="",
    )
) -> None:
    template = """
[Unit]
Description=atlasNode daemon
After=network-online.target

[Service]
Type=simple
Restart=always
RestartSec=1
WorkingDirectory={}
ExecStart={}atlas --password {} --datadir {} --syncmode full --port 30321 --mine --miner.validator {}  --unlock {}
SyslogIdentifier=atlasNode
StartLimitInterval=0
LimitNOFILE=65536
LimitNPROC=65536

[Install]
WantedBy=multi-user.target
"""

    sysd = template.format(*[x for x in context.values()])
    log.info(sysd)
    save_file("atlasNode.service", sysd)
    return sysd