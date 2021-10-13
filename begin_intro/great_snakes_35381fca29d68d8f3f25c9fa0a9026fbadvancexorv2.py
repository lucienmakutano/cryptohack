from pwn import xor


def hex_(string):
    return bytes.fromhex(string)


key1 = hex_(
    "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

# try all possible numbers between 0 and 255
for i in range(0, 256):
    result = xor(key1, i)
    print(result)

# result = xor(key1, key2)
# print(result)
# crypto{0x10_15_my_f4v0ur173_by7e}
