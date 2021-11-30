# get public key
pk_uncompressed_with_prefix = "0x040dc6785daab4f31d390cf53a9c04a39088380ac9d4828da48f5e90273d51bb0ceaac56d963074282d87907d98487ba9c29e5719409c4cc42c8d646ae7c190b42"
pk_uncompressed = pk_uncompressed_with_prefix[4:]
pk_uncompressed_bytes = bytes.fromhex(pk_uncompressed)

# keccak hash
from Crypto.Hash import keccak
keccak_hash = keccak.new(digest_bits=256)
keccak_hash.update(pk_uncompressed_bytes)
keccak_hash_digest = keccak_hash.hexdigest()

# ETH address (0x prefix with last 20 bytes of keccak_hash_digest
ETH_address = "0x"+ keccak_hash_digest[-40:]
print(ETH_address)

