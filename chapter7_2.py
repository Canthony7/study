# --*-- coding:utf-8 --*--

import requests

url = "http://localhost:8050/render.html"
params = {
    "url": "https://www.autohome.com.cn/spec/35194/#pvareaid=2042128",
    "height": "50",
    "width": "50"
}

res = requests.get(url, params=params)
print(res.text)
with open("test.png", "wb") as f:
    f.write(res.content)


