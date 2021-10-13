key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
r2 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
r3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

def xor(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

xored = xor(key1, xor(r2, r3))
print(bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"))
