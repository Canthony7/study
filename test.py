# --*-- coding:utf-8 --*--
import requests
from requests.packages import urllib3

# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456789")
#
# r = s.get("http://httpbin.org/cookies")
#
# print(r.text)

res = requests.get("https://www.12306.cn/", verify=False)
print(res.status_code)
