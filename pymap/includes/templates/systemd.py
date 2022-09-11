atlasNode = """
[Unit]
Description=atlasNode daemon
After=network-online.target

[Service]
Type=simple
Restart=always
RestartSec=1
WorkingDirectory={}
ExecStart={}atlas --password {} --datadir {} --syncmode full --port 30321 --v5disc --mine --miner.validator {}  --unlock {} {}
SyslogIdentifier=atlasNode
StartLimitInterval=0
LimitNOFILE=65536
LimitNPROC=65536

[Install]
WantedBy=multi-user.target
"""

monitorService = """
[Unit]
Description=atlasMonitorService daemon
After=network-online.target

[Service]
Type=simple
Restart=always
RestartSec=1
WorkingDirectory={}/pymap
ExecStart=python3 run_monitor.py
SyslogIdentifier=atlasMonitorService
StartLimitInterval=0
LimitNOFILE=65536
LimitNPROC=65536

[Install]
WantedBy=multi-user.target
"""
