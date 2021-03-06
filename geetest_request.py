import random
import execjs
import rsa
import binascii
import requests
import re
import time
from geetest_image import get_distance
from geetest_source_track import source_track


# fullpage
def get_js3():
    f = open("fullpage.js", 'r', encoding='utf-8')  # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


# fullpage
def fullpages():
    jsstr = get_js3()
    ctx = execjs.compile(jsstr)  # 加载JS文件
    return (ctx.call('ddd'))  # 调用js方法  第一个参数是JS的方法名，后面的data是js方法的参数


# 6772 6786
def Vd_my():
    b = int((65536 * (1 + random.random())))
    a = hex(b).replace('0x', '')[1:]
    message = a + a + a + a
    message = message.encode()
    return message


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


# Q0o
def get_js():
    f = open("my_e2.js", 'r', encoding='utf-8')  # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


# Q0o
def parse(I1P, Vd):
    jsstr = get_js()
    ctx = execjs.compile(jsstr)  # 加载JS文件
    return (ctx.call('eee', I1P, Vd))  # 调用js方法  第一个参数是JS的方法名，后面的data是js方法的参数


def parse_res():
    session = requests.session()
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Host': 'www.vipkid.com.cn',
        'Referer': 'https://www.vipkid.com.cn/login',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
    }
    # 请求得到gt和challenge参数
    res = session.post(
        url='https://www.vipkid.com.cn/rest/ucaccount/account/verifycode/login/sms'
        , data={'mobile': '15934117585',
                'type': '1',
                'appId': '10001',
                'domain': 'www.vipkid.com.cn'
                }, headers=headers, verify=False)
    gt = res.headers.get('vk-gt')
    challenge = res.headers.get('vk-gt-challenge')
    print("旧的challenge：{}与gt:{}".format(challenge,gt))
    print(res.text)
    headers.update({'Host': 'api.geetest.com'})

    # 这里set_cookie一个 GeeTestUser 返回一些js版本信息
    res2 = session.get(
        url='https://api.geetest.com/gettype.php?gt={}&callback=geetest_{}'.format(gt, int(time.time() * 1000)),
        headers=headers,
        verify=False)
    print(res2.text)
    # 其中有部分参数是从res2.text来 ，i是浏览器的参数
    # i = fullpages()
    # param1 = '''{"gt":"%s", "challenge": "%s", "offline": false, "new_captcha": false, "product": "bind", "width": "280px","protocol": "https://","static_servers":["static.geetest.com/","dn-staticdown.qbox.me/"],"aspect_radio":{"pencil":128,"voice":128,"slide":103,"click":128,"beeline":50},"slide":"/static/js/slide.7.4.3.js","click":"/static/js/click.2.6.4.js","pencil":"/static/js/pencil.1.0.1.js","voice":"/static/js/voice.1.1.4.js","beeline":"/static/js/beeline.1.0.1.js","type":"fullpage","fullpage":"/static/js/fullpage.8.6.1.js","geetest":"/static/js/geetest.6.0.9.js","cc": 4, "ww": true, "i": "%s"}''' % (
    #     gt, challenge, i)
    # print(param1)
    # message = Vd_my()  # 随机16位
    # t0o = rsa_my(message)
    # message = message.decode()
    # Q0o = parse(I1P=param1, Vd=message)  # aes加密
    # w1 = Q0o + t0o
    # print("生成的w值为{}".format(w1))
    # 返回一些不知道用来干嘛的信息
    res3 = session.get(
        url='https://api.geetest.com/get.php?gt={}&challenge={}&lang=zh-cn&pt=0&callback=geetest_{}'.format(
            gt, challenge, int(time.time() * 1000)),
        headers=headers,
        verify=False)
    print("第三个请求{}".format(res3.text))

    # 这个请求set_cookie GeeTestAjaxUser
    res4 = session.get(
        url='https://api.geetest.com/ajax.php?gt={}&challenge={}&lang=zh-cn&pt=0'.format(
            gt, challenge),
        headers=headers,
        verify=False, )
    print("第4个请求{}".format(res4.text))
    print("第4个请求headers为:::{}".format(res4.headers))
    print("第4个请求cookies为:::{}".format(session.cookies))

    res5 = session.get(
        url='https://api.geetest.com/get.php?is_next=true&type=slide3&gt={}&challenge={}&lang=zh-cn&https=false&protocol=https%3A%2F%2F&offline=false&product=embed&api_server=api.geetest.com&width=100%25&callback=geetest_{}'.format(
            gt, challenge, int(time.time() * 1000)),
        headers=headers,
        verify=False)
    print("第5个请求url为:::{}".format(res5.url))
    print("第5个请求text:{}".format(res5.text))
    full1 = re.findall(re.compile(r'"fullbg": "(.*?)",'), str(res5.text))
    slice1 = re.findall(re.compile(r'"bg": "(.*?)",'), str(res5.text))
    new_challenge = re.findall(re.compile(r'"challenge": "(.*?)",'), str(res5.text))

    if full1 and slice1 and new_challenge:
        full1 = full1[0]
        slice1 = slice1[0]
        new_challenge = new_challenge[0]
        print("得到新的new_challenge:{}".format(new_challenge))
        print("得到新的new_gt:{}".format(gt))
        full_picture_url = "https://static.geetest.com/" + full1
        slice_picture_url = "https://static.geetest.com/" + slice1
        print("full_picture_url图片地址{}".format(full_picture_url))
        print("slice_picture_url图片地址{}".format(slice_picture_url))
        headers.update({'Host': 'static.geetest.com'})
        response_image1 = session.get(url=full_picture_url, headers=headers, verify=False)
        response_image2 = session.get(url=slice_picture_url, headers=headers, verify=False)
        with open('full.webp', 'wb') as f:
            f.write(response_image1.content)
            print('full.webp生成成功')
        with open('slice.webp', 'wb') as f:
            f.write(response_image2.content)
            print('slice.webp生成成功')
        distance = get_distance()
        print('距离成功生成：{}'.format(distance))
        session.cookies.clear()
        # 从轨迹池挑选轨迹
        track_list1 = get_track(distance=distance)
        return track_list1, gt, new_challenge, session


def get_track(distance):
    """
    根据偏移量获取移动轨迹
    :param distance: 偏移量
    :return: 移动轨迹
    """
    # 移动轨迹
    track = []
    a1 = -random.randint(12, 35)
    track.append([a1, a1 - random.randint(1, 10), 0])
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 0
    time = 0
    while current < distance:
        if current < mid:
            # 加速度为正2
            a = 2
            y = 0
        else:
            # 加速度为负3
            y = -1
            a = -3
        # 初速度v0
        v0 = v
        # 当前速度v = v0 + at
        v = v0 + a * t
        # 移动距离x = v0t + 1/2 * a * t^2
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        time += t * 100
        current += move
        # 加入轨迹
        track.append([int(current), y, int(time)])
    return track


if __name__ == '__main__':
    # print(parse(I1P="""""", Vd=""))
    # print(get_track(distance=71))
    print(fullpages())
