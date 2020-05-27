#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 19:45
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.3pachong_requests.py
# @Software: PyCharm

# get请求
import requests

url = 'http://httpbin.org/get'
data = {'key': 'value', 'abc': 'xyz', 'a': '123'}
# .get是使用get方式请求url，字典类型的data不用进行额外处理
response = requests.get(url, data)
print(response.text)
print("----------------------")

# # post请求
import requests

url = 'http://httpbin.org/post'
data = {'key': 'value', 'abc': 'xyz', 'a': '123'}
# .post表示为post方法
response = requests.post(url, data)
# 返回类型为json格式
print(response.json())
print("----------------------")