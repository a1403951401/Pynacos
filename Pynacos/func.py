import json
import requests
from time import sleep

from hashlib import md5
from Pynacos.Err import Request_Err

# unicode char (1) char(2)
u1 = u'\x01'
u2 = u'\x02'


# 检查网页状态的方法
def check(html, json = True):
    code = html.status_code
    if code == 200:
        if html.text == "ok":
            return True
        if json:
            try:
                return html.json()
            except:
                pass
        return html.text
    else:
        print(html.text)
        raise Request_Err(code)


# 拼接链接的方法
def getUrl(ip, port, more):
    return f"http://{ip}:{port}{more}"

def getMD5(txt):
    return md5(str(txt).encode("utf-8")).hexdigest()
