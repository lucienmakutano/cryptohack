from pwn import xor


def hex_(string):
    return bytes.fromhex(string)


key1 = hex_("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

# try all possible numbers between 0 and 255
# for i in range(0, 256):
#     result = xor(key1, i)
#     print(result)

result = xor(key1, 16)
print(result)
# crypto{0x10_15_my_f4v0ur173_by7e}
