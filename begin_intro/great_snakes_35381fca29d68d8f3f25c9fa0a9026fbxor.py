# from pwntools import *

char_to_num = {
    "a": 97,
    "b": 98,
    "e": 101,
    "l": 108,
}

def to_bin(num):
    res = ""
    while num != 0:
        bina = num % 2
        num //= 2
        res = str(bina) + res

    return res

def to_str(num):
    str_num = str(num)
    res = 0
    
    for i, c in enumerate(list(str_num)):
        res += (2 ** i) * int(c)
    
    return res

def xor(num, xorer):
    is_bigger = len(str(num)) > len(str(xorer))
    compl_xorer = ""
    str_num = str(num)
    str_xorer = str(xorer)
    xor_res = ""

    if is_bigger:
        diff = len(str_num) - len(str_xorer)
        compl_zeros = diff * "0"
        compl_xorer = compl_zeros + str_xorer
    
    for i in range(len(str(num))):
        if str_num[i] == compl_xorer[i]:
            xor_res = "0" + xor_res
        else:
            xor_res = "1" + xor_res
    
    return xor_res

if __name__ == '__main__':
    strs = list("label")
    bin_13 = to_bin(13)

    for s in strs:
        num = char_to_num.get(s)
        corr_bin = to_bin(num)
        res_xor = xor(corr_bin, bin_13)
        print corr_bin
        print(to_str(res_xor))

