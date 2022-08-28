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
binaries=/home/atlas/build/bin
rpcaddr=https://poc3-rpc.maplabs.io
rpcport=False
keystore=
password=password
passwordFile=/home/password
namePrefix=validator
lockedNum=1000000
signerPriv=0x
validator=0x
voteNum=10000
commission=40000
datadir=werwerrrrrrrrrrrrrrrrrr
miner.validator=0x
unlock=0x
syncmode=full
port=30321
validator_wallet=0x

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


