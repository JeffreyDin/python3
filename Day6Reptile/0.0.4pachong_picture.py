#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 9:12
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.4pachong_picture.py
# @Software: PyCharm


import requests
import re
content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
print(content)