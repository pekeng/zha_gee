#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import rsa
import binascii


def en_test():
    param_1 = "10001"
    # 某次我找到的
    param_2 = "00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81"
    message = b'77d3aa236f81751e'
    modulus = int(param_2, 16)
    print(modulus)
    exponent = int(param_1, 16)
    print(exponent)
    rsa_pubkey = rsa.PublicKey(modulus, exponent)
    print(rsa_pubkey)
    crypto = rsa.encrypt(message, rsa_pubkey)
    print(crypto)
    data = binascii.b2a_hex(crypto)
    print(data)
    print(data.decode('utf-8'))


if __name__ == '__main__':
    en_test()
