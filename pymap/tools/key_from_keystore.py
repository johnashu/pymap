import hashlib
from pymap.tools.file_op import open_json
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Hash import keccak


def pk_from_store(fn: str, password: str) -> None:

    keystore = open_json(fn)
    address = fn.split("--")[-1]

    dec_key = hashlib.scrypt(
        bytes(password, "utf-8"),
        salt=bytes.fromhex(keystore["crypto"]["kdfparams"]["salt"]),
        n=keystore["crypto"]["kdfparams"]["n"],
        r=keystore["crypto"]["kdfparams"]["r"],
        p=keystore["crypto"]["kdfparams"]["p"],
        maxmem=2000000000,
        dklen=keystore["crypto"]["kdfparams"]["dklen"],
    )

    decoded = dec_key[16:] + bytes.fromhex(keystore["crypto"]["ciphertext"])

    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(decoded)
    validated = keccak_hash.hexdigest()
    print("Validated: ", validated)

    iv_int = int(keystore["crypto"]["cipherparams"]["iv"], 16)
    ctr = Counter.new(
        AES.block_size * keystore["crypto"]["kdfparams"]["r"], initial_value=iv_int
    )
    dec_suite = AES.new(dec_key[0:16], AES.MODE_CTR, counter=ctr)
    plain_key = dec_suite.decrypt(bytes.fromhex(keystore["crypto"]["ciphertext"]))
    pk = plain_key.hex()

    print(f"\n\tAddress:  {address}\n\tPrivate Key:  {pk}")
