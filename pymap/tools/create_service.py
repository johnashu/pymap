from pymap.tools.file_op import save_file

template = """
cat<<-EOF > /etc/systemd/system/atlasNode.service
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
EOF

"""


def create_systemd(
    context: dict = dict(
        working_dir="/root",
        binary="/root/atlas/build/bin/atlas",
        password="password",
        datadir="/root/pymap/admin",
        validator="0x64a1c184fd6ed7a064102619ae77fda7cc29ceb8",
        unlock="0x64a1c184fd6ed7a064102619ae77fda7cc29ceb8",
    )
) -> None:
    sysd = template.format(*[x for x in context.values()])
    print(sysd)
    return sysd
