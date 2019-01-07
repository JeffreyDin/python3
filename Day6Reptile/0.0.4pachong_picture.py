#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 9:12
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.4pachong_picture.py
# @Software: PyCharm


import requests
import re

# 使用get方法 内容
content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
print(content)
print("----------------------")

# <div class="grid-item work-thumbnail">
# <a href="http://www.cnu.cc/works/299164" class="thumbnail" target="_blank">
# <div class="title"> "我的一千零一首情歌（中）”</div>
# <div class="author"> darling安老师 </div>

# 不能使用贪婪模式
# <div class="grid-item work-thumbnail">
# <a href="(.*?)" class="thumbnail" target="_blank">
# <div class="title">(.*?)</div>
# <div class="author"> darling安老师 </div>

# <div class="grid-item work-thumbnail">
# <a href="(.*?)".*?title">(.*?)</div>
# <div class="author"> darling安老师 </div>

# pattern模式，样品 results 结果，成绩
pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(pattern, content)
print(results)

for result in results:
    url, name = result
    print(url, re.sub('\s', '', name))
