#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Farr Ding  Time: 2018/6/12


# name = "DJ ZhangYang YanYun WangYa"
names = ["DJ", "ZhangYang", "YanYun", "WangYa", "LiLei"]
names.insert(1, "FFF")     # 插入，1——>下标
names.insert(3, "FFF")     # 插入，3——>下标
names[4] = "DDD"            # 替换
print(names)
# 索引之查找DDD的位置
# print(names.index("DDD"))
# print(names[names.index("DDD")])

names2 = ['1', '5', 'FFF', 'DJ']
# 合并，如果不删除names2，仍然存在
names.extend(names2)
del names2
print(names)




# 排序
# names.sort()
# print(names)
# names2 = ['LiLei', '#!WangYa', '4DDD', 'aFFF', 'ZhangYang', 'FFF', 'DJ']
# names2.sort()
# print(names2)

# 反转
#names.reverse()
#print(names)




# 清空
# names.clear()
# print(names)

# 统计同名
# print(names.count("FFF"))


# delete
# names.remove("DDD")
# del names[3]  =names.pop(3)
# names.pop()                  # 如果不输入下标，默认删除最后一个








'''
# 切片
names = ["DJ", "ZhangYang", "YanYun", "WangYa", "LiLei"]
print(names)
print(names[0], names[2])
print(names[1:3])       # 切片，顾头不顾尾！取位置为1~2的字符串
print(names[-1])        # 切片，从左往右数，-4，-3，-2，-1   取最后一个元素
print(names[-2:])       # 切片，取最后两个值
print(names[-3:-1])     # 切片，从左往右数，顾头不顾尾！取倒数第三个和倒数第二个元素
print(names[0:3])       # 切片，0可以省略，取前三个元素

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number[0:10:1])   # 0，1全部可省略
print(number[:])        # print(number[:]) = print(number[:10]) = print(number[:100])
print(number[::2])
print(number[1::2])
print(number[2::3])     # 切片，从第二个元素开始，第一个元素的索引（下标）为0，那么3的索引为2，每隔3位取一个元素

'''

