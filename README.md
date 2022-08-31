# pymap

Python interface for validators for interacting with the MAP protocol

# Install Python / pip

```bash
sudo apt update && sudo apt upgrade -y

apt install python3-pip

pip3 install -r requirements.txt
```

# Create .env file

Data to be included in the `.env` file.  

Some of this information will be gathered during setup and will need to be updated as required.


```bash
binaries=/home/maffaz/atlas/build/bin
testnet=http://18.142.54.137:7445
rpcaddr=https://poc3-rpc.maplabs.io
rpcport=False
password=password
passwordFile=/home/maffaz/password
keystore=/home/maffaz/node/keystore/UTC--2022-08-26T23-45-19.943014769Z--1234567890abcdef123456
namePrefix=validator
lockedNum=10
signerPriv=
validator=0x
target=0x
voteNum=5
commission=40000
datadir=admin
miner.validator=0x
unlock=0x
syncmode=full
port=30321
default_address=0x

```

run `example.py` to get started..


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
ExecStart=/home/maffaz/atlas/build/bin/atlas --password password --datadir /home/maffaz/node --syncmode full --port 30321 --mine --miner.validator 0x53d923e76645f7d91e1f27d08339937f5aefcb62  --unlock 0x53d923e76645f7d91e1f27d08339937f5aefcb62
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


