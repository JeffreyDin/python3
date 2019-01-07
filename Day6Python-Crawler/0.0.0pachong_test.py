#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 18:48
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.0pachong_test.py
# @Software: PyCharm

# 导入urllib库稍微有些区别
# import urllib
# urllib.request
# 正确导入方式：
from urllib import request

url = "http://www.baidu.com"
# request.urlopen解析内容，类似浏览器打开网页，设置超时时间
response = request.urlopen(url, timeout=1)
# read 读取内容
print(response.read().decode('utf-8'))

# gbk 一个英文一个位置。一个汉字两个位置(仅包含常用字)
# utf-8 一个汉字三个位置(包含生僻字)

# 学习内容：
# 请求网页的方式get和post
# 测试http地址：http://httpbin.org/
# http://httpbin.org/get?a=123&b=456
# https://www.infoq.cn/

# 正常get请求的方式：
# http://httpbin.org/get?a=123&b=456
# {
#   "args": {
#     "a": "123",
#     "b": "456"
#   },
#   "headers": {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
#     "Connection": "close",
#     "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
#     "Host": "httpbin.org",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
#   },
#   "origin": "119.254.228.2",
#   "url": "http://httpbin.org/get?a=123&b=456"
# }