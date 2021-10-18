# using euclid's algorithm

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


print(gcd(12, 8))
print(gcd(66528, 52920))
print(gcd(12, 8))
