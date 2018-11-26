#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Farr Ding  Time: 2018/7/20

# 字典一个特性，没有下标，乱序
info = {
    'stu101': "TengLan Wu",
    'stu102': "longZe Luola",
    'stu103': "XiaoZe Maliya"
}

print(info)
# print(info["stu101"])

'''
# add 
info["stu101"] = "武藤兰"  # 修改
info["stu104"] = "Cangjingkong"  # 不存在，创建
print(info)

# del
info.pop("stu101")   # 如果不指定，随机删
# del info["stu101"]
# info.popitem()        # 随机删
print(info)


# find
print(info.get("stu104"))
# Determine whether the dictionary has data
print('stu104' in info)   # info.has_key("103")  in py2.x


# 分别打印values  keys
print(info.values())
print(info.keys()）


# setdefault  在字典中取值，取到，将stu103返回，取不到stu106，创建
print(info.setdefault("stu103","Alex"))
print(info)
print(info.setdefault("stu106","Alex"))
print(info)

# update 字典合并，原有且更改的，更新；原没有的，增加
b = {
    "stu101": "Daqiao",
    1: 3,
    2: 4
}
info.update(b)
print(info)


# items 将字典转化成列表
print(info.items())


# [1, {"name": "alex"}, 444] 共用一个地址空间，类似浅copy
c = dict.fromkeys([6, 7, 8], "test")
c2 = dict.fromkeys([6, 7, 8], [1, {"name": "alex"}, 444])
print(c)
print(c2)
c2[7][1]['name'] = "jack"
print(c2)

'''
# 高效 通过索引，直接取出info
for i in info:
    print(i, info[i])
print("----------")
# 低效  将字典转成列表（数据量很大时，转很长时间，机器奔溃）   列表中每一个元素都是一个小元组
for k, v in info.items():
    print(k, v)



