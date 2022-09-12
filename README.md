# pymap

Python interface for validators for interacting with the MAP protocol

# Install Python / pip

```bash
sudo apt update && sudo apt upgrade -y

apt install python3
apt install python3-pip

pip3 install -r requirements.txt
```

# Create .env file

Data to be included in the `.env` file.  

Some of this information will be gathered during setup and will need to be updated as required.

see `example.env` for an explanation and starting point


run `start_tool.py` to get started..


# Service control.

```bash
cat<<-EOF > /etc/systemd/system/atlasNode.service
[Unit]
Description=atlasNode daemon
After=network-online.target

[Service]
Type=simple
Restart=always
RestartSec=1
WorkingDirectory=/home/maffaz
ExecStart=/home/maffaz/atlas/build/bin/atlas --password password --datadir /home/maffaz/node --syncmode full --port 30321 --mine --miner.validator <Signer Address>  --unlock <Signer Address>
SyslogIdentifier=atlasNode
StartLimitInterval=0
LimitNOFILE=65536
LimitNPROC=65536

[Install]
WantedBy=multi-user.target

EOF

```

a password file is required for the service to run correctly!


```bash


sudo mv atlasNode.service /etc/systemd/system/atlasNode.service
sudo service atlasNode stop
sudo systemctl daemon-reload 
sudo chmod 644 /etc/systemd/system/atlasNode.service
sudo systemctl enable atlasNode.service
sudo service atlasNode start

```
  
# Check Logs
tail -f /var/log/syslog

# Monitoring

edit `alerts.example.env` and save as `alerts.env`

run monitor to check.  It will always send an email when starting

`python3 run_monitor.py`

Select option  3 from the title screen to create and run monitor service

> Vote / Stake with Maffaz Node: https://staking.maplabs.io/#/login?redirect=%2FaddVote%2F0x1C45F8a4C8b34ecf5Ee2F6208896B782D04FE006

> Donations welcome: 0x4F35285F1c387394197A0cdeA16D3a0eAA2c58F5