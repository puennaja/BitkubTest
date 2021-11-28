# example data (hex string with prefix)
pk_uncompressed = "0x040dc6785daab4f31d390cf53a9c04a39088380ac9d4828da48f5e90273d51bb0ceaac56d963074282d87907d98487ba9c29e5719409c4cc42c8d646ae7c190b42"
pk_compressed = "0x020dc6785daab4f31d390cf53a9c04a39088380ac9d4828da48f5e90273d51bb0c"

# get x and y
pk_uncompressed_no_prefix = pk_uncompressed[4:]
pk_uncompressed_x = pk_uncompressed_no_prefix[:len(pk_uncompressed_no_prefix)//2]
pk_uncompressed_y = pk_uncompressed_no_prefix[len(pk_uncompressed_no_prefix)//2:]

# compress
pk_int_uncompressed_y = int(pk_uncompressed_y, 16) # hex to int with no prefix
pk_new_compressed = ""
if pk_int_uncompressed_y % 2 == 0:
    pk_new_compressed = "0x02" + pk_uncompressed_x
else:
    pk_new_compressed = "0x03" + pk_uncompressed_x

# check is OK
if pk_compressed == pk_new_compressed:
    print(pk_new_compressed)
    print("Compressed OK")
else:
    print("Compressed Fail")