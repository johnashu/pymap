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
keystore=/home/maffaz/pymap/admin/keystore/UTC--2022-08-26T23-45-19.943014769Z--1234567890abcdef123456
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

```

run `example.py` to get started..


# Service control.


a password file is required for the service to run correctly!


```bash

 chmod +x startNode.sh

 chmod 644 /etc/systemd/system/atlasNode.service

 service atlasNode stop

 systemctl daemon-reload 
 
 systemctl enable atlasNode.service

 service atlasNode start

 service atlasNode status

```
 
# Check Logs
tail -f /var/log/syslog


