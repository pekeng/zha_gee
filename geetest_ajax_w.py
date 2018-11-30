import random
import execjs
import rsa
import binascii
import time


def get_js():
    f = open("i8.js", 'r', encoding='utf-8')  # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


# data=gt+change(顺序不能反)MD5加密
def Ii8(data):
    jsstr = get_js()
    ctx = execjs.compile(jsstr)  # 加载JS文件
    return ctx.call('I8', data)  # 调用js方法  第一个参数是JS的方法名，后面的data是js方法的参数


# fullpage
def get_js3():
    f = open("fullpage.js", 'r', encoding='utf-8')  # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


# magic 正确 ip要改。。。
def fullpages1():
    jsstr = get_js3()
    ctx = execjs.compile(jsstr)  # 加载JS文件
    return (ctx.call('magic'))  # 调用js方法  第一个参数是JS的方法名，后面的data是js方法的参数


def fullpages2():
    jsstr = get_js3()
    ctx = execjs.compile(jsstr)  # 加载JS文件
    return (ctx.call('ddd'))  # 调用js方法  第一个参数是JS的方法名，后面的data是js方法的参数


# 6135
def rsa_my(message):
    param_1 = "10001"
    # 公钥
    param_2 = "00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81"
    modulus = int(param_2, 16)
    exponent = int(param_1, 16)
    rsa_pubkey = rsa.PublicKey(modulus, exponent)
    crypto = rsa.encrypt(message, rsa_pubkey)
    data = binascii.b2a_hex(crypto).decode()
    return data


# "M(*((1((M(("的js
def get_js():
    f = open("fullpage2.js", 'r', encoding='utf-8')  # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


# t8的md5的js
def get_t8_js():
    f = open("i8.js", 'r', encoding='utf-8')  # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


# "M(*((1((M(("的调用
def p0o():
    jsstr = get_js()
    ctx = execjs.compile(jsstr)  # 加载JS文件
    return ctx.call('kill_mouse')  # 调用js方法  第一个参数是JS的方法名，后面的data是js方法的参数


# 确认正确
def M5(data1, data2, data3):
    jsstr = get_js()
    ctx = execjs.compile(jsstr)  # 加载JS文件
    return ctx.call('kill_M5', data1, data2, data3)  # 调用js方法  第一个参数是JS的方法名，后面的data是js方法的参数


def M52(data):
    jsstr = get_js()
    ctx = execjs.compile(jsstr)  # 加载JS文件
    return ctx.call('kill_Md5', data)  # 调用js方法  第一个参数是JS的方法名，后面的data是js方法的参数


def t8(data):
    jsstr = get_t8_js()
    ctx = execjs.compile(jsstr)  # 加载JS文件
    return ctx.call('I8', data)  # 调用js方法  第一个参数是JS的方法名，后面的data是js方法的参数


def ajax_w():
    PO0 = p0o()
    cc = [12, 58, 98, 36, 43, 95, 62, 15, 12]
    s = "43692e50"
    ep = """{"ts": 1543484414538, "v": "8.6.4", "ip": "192.168.1.210,218.26.185.2",
          "f": "d1b1ec3607d6a88a1e59151e19a70a1f", "de": false, "te": false, "me": true, "ven": "Google Inc.",
          "ren": "ANGLE (Intel(R) HD Graphics 630 Direct3D11 vs_5_0 ps_5_0)", "ac": "f930496cb2084fa8e08a507beb9e3871",
          "pu": false, "ph": false, "ni": false, "se": false, "fp": null, "lp": null,
          "em": {"ph": 0, "cp": 0, "ek": "11", "wd": 0, "nt": 0, "si": 0, "sc": 0},
          "tm": %s,
          "by": 2}"""
    gt = ""
    # 之前的challenge
    challenge = ""
    passtime = 15788 + random.randint(100, 200)
    h0o = {
        'lang': "zh-cn",
        'type': "fullpage",
        'tt': M5(PO0, cc, s),
        's': t8(M52(data=PO0)),
        'h': t8(M52(data=fullpages1())),
        'hh': t8(fullpages1()),
        'hi': t8(fullpages2()),
        'ep': ep,
        'passtime': passtime,  # 这时间是程序运行的时间 有叠加的
        "rp": Ii8(data=gt + challenge + str(passtime))  # md5
    }


if __name__ == '__main__':
    PO0 = p0o()
    print(M52(data=PO0))
    print(t8(M52(data=PO0)))
