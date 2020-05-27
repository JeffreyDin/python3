#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 19:07
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.1pachong_test.py
# @Software: PyCharm

# request用来发起请求
# parse用来处理post数据
from urllib import request
from urllib import parse

# # post请求，urllab需要封装数据，使用parse.urlencode对数据进行封装，用request.urlopen打开网页，使用data指定数据
# data = bytes(parse.urlencode({"word": "hello"}), encoding='utf-8')
# # print()
#
# response = request.urlopen('http://httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

# # get，建议使用urlopen时，为了防止程序卡死，带上timeout参数
# # User-Agent反应当前get请求的应用
# response2 = request.urlopen('http://httpbin.org/get', timeout=1)
# print(response2.read())

# # urllib.error.URLError: <urlopen error timed out>超时
# response3 = request.urlopen('http://httpbin.org/get', timeout=0.1)

# 使用try进行错误捕获
import urllib
import socket
# 请求错误一般发生在套接字层面，需要导入socket库，套接字连接超时

try:
    response4 = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT!')

