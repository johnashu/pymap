# pymap

Python interface for validators for interacting with the MAP protocol

# Install Python / pip

sudo apt update && sudo apt upgrade -y

apt install python3-pip

pip3 install -r requirements.txt


# Create env file

Data to be included in the `.env` file.  

Some of this information will be gathered during setup and will need to be updated as required.


```bash
binaries=/atlas/build/bin
rpcaddr=127.0.0.1
rpcport=7445
keystore=~/test/keystore/UTC--2022-08-17T17-41-16.086417459Z--635dad5a10ddd1662517dc85e3bc4ca9ce9f6f03
password=password
namePrefix=validator
lockedNum=1000000
signerPriv="0x"
validator="0x"
voteNum=10000
```

run `example.py` to get started..

# Check Logs
tail -f /var/log/syslog