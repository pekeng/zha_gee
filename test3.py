# /usr/bin/python
# encoding: utf-8

import base64


def str2key(s):
    # 对字符串解码
    b_str = base64.b64decode(s)
    # print(b_str)
    if len(b_str) < 162:
        return False

    hex_str = ''

    # 按位转换成16进制
    for x in str(b_str):
        h = hex(ord(x))[2:]
        h = h.rjust(2, '0')
        hex_str += h

    # 找到模数和指数的开头结束位置
    m_start = 29 * 2
    e_start = 159 * 2
    m_len = 128 * 2
    e_len = 3 * 2

    modulus = hex_str[m_start:m_start + m_len]
    exponent = hex_str[e_start:e_start + e_len]

    return modulus, exponent


if __name__ == "__main__":
    pubkey = "9a39c3fefeadf3d194850ef3a1d707dfa7bec0609a60bfcc7fe4ce2c615908b9599c8911e800aff684f804413324dc6d9f982f437e95ad60327d221a00a2575324263477e4f6a15e3b56a315e0434266e092b2dd5a496d109cb15875256c73a2f0237c5332de28388693c643c8764f137e28e8220437f05b7659f58c4df94685"
    key = str2key(pubkey)
    print(key)
