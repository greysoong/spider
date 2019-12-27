# -*- coding: UTF-8 -*-
"""
file:spide001.py
data:2019-12-109:39
author:Grey
des:
"""

from requests import Session,Request,get
import requests
import re
from requests.auth import HTTPBasicAuth

url = 'http://stockpage.10jqka.com.cn/600139/funds/'
data = {
    'name':'germey'
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}
s = Session()
r = s.get(url,headers=headers)

print (r.text)
