# get public key
pk_compressed_with_prefix = "0x020dc6785daab4f31d390cf53a9c04a39088380ac9d4828da48f5e90273d51bb0c"
pk_compressed = pk_compressed_with_prefix[4:]
pk_compressed_bytes = bytes.fromhex(pk_compressed) 

from Crypto.Hash import SHA256,RIPEMD160

# HASH SHA256
h256 = SHA256.new(data=pk_compressed_bytes)
h256_hexstr = h256.hexdigest()

# HASH RIPEMD160
h256_hexbytes = bytes.fromhex(h256_hexstr) 
h160 = RIPEMD160.new(data=h256_hexbytes)
h160_hexstr = h160.hexdigest()

# Add prefix version 00 means Bitcoin Address
h160_hexstr_prefix = "00" + h160_hexstr
h160_hexbytes_prefix = bytes.fromhex(h160_hexstr_prefix) 

# get check sum from 4 first of sha256(sha256(h160_hexstr_prefix))
# hash256 seq 1
h256_of_h160_with_prefix = SHA256.new(data=h160_hexbytes_prefix)
h256_of_h160_with_prefix_hexbytes = bytes.fromhex(h256_of_h160_with_prefix.hexdigest())
# hash256 seq 2
h256_of_h256_of_h160_hex_with_prefix = SHA256.new(data=h256_of_h160_with_prefix_hexbytes)
h256_of_h256_of_h160_hex_with_prefix_hexstr = h256_of_h256_of_h160_hex_with_prefix.hexdigest()
check_sum = h256_of_h256_of_h160_hex_with_prefix_hexstr[:8]

# get BTC address in hex string
BTC_address_hexstr = h160_hexstr_prefix + check_sum
binary_BTC_address_bytes = bytes.fromhex(BTC_address_hexstr)

# encode to base58 string
import base58check
BTC_address_bytes = base58check.b58encode(binary_BTC_address_bytes)
BTC_address_str = BTC_address_bytes.decode()
print(BTC_address_str)