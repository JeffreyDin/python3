#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Farr Ding  Time: 2018/7/20


name = "my name is alex"
print(name.capitalize())          # 首字母大写
print(name.count("a"))            # 统计a的个数
print(name.center(50, "-"))       # 美观打印，打印50个字符，不够用-补上
print(name.encode(encoding="utf-16"))  # 使用utf-16将字符串转化为bytes
print(name.endswith("ex"))  # 判断一个字符串以什么结尾（判断邮件地址是否以.com结尾）
# name = "my \tname is alex"
print(name.expandtabs(tabsize=30))  # 将 Tab键转换成多少个空格
print(name.find("n"))            # 查找,字符串的索引
print(name[name.find("name"):])   # 字符串可以切片，从name开始截断

