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




> Donations welcome: 0x4F35285F1c387394197A0cdeA16D3a0eAA2c58F5