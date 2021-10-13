from operator import xor


def hex_(string):
    return bytes.fromhex(string)


def bitwise_xor_bytes(a, b):
    result_int = int.from_bytes(
        a, byteorder="big") ^ int.from_bytes(b, byteorder="big")
    return result_int.to_bytes(max(len(a), len(b)), byteorder="big")


key1 = hex_("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
r2 = hex_("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
r3 = hex_("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

result = bitwise_xor_bytes(key1, bitwise_xor_bytes(r2, r3))

print(result)
