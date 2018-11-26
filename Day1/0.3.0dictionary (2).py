#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Farr Ding  Time: 2018/7/20

av_catalog = {
    "欧美": {
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大", "质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
        "x-art.com": ["质量很高,真的很高", "全部收费,屌比请绕过"]
    },
    "日韩": {
        "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "听说是收费的"]
    },
    "大陆": {
        "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
    }
}

av_catalog["大陆"]["1024"][1] += ",可以用爬虫爬下来"
print(av_catalog["大陆"]["1024"])
av_catalog.setdefault("大陆",{"www" : [1,2]})
print(av_catalog)
#ouput
['全部免费,真好,好人一生平安', '服务器在国外,慢,可以用爬虫爬下来']

# name = "my name is {name} and i am {years} old."
# print(name.format(name='alex', years=23))  # 格式化
# print(name.format_map({'name': 'alex', 'years': 12}))  # 字典，格式化
