#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 19:35
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.2pachong_http_headers.py
# @Software: PyCharm

# request用来发起请求
# parse用来处理post数据
from urllib import request, parse

url = 'http://httpbin.org/post'
# http头部信息的模拟
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://httpbin.org/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

dict = {
    'name': 'value'
}

# post请求，urllab需要封装数据，使用parse.urlencode对数据进行封装，用request.urlopen打开网页，使用data指定数据
data = bytes(parse.urlencode(dict), encoding='utf8')
# 重新定义Request
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))



