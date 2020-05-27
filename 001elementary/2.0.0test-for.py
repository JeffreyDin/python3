#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Jianfeng Ding  Time: 2018/11/20

# for循环可以遍历任何序列的项目，如一个列表或者一个字符
# loop循环
# languages = ["C", "C++", "Perl", "Python"]
# for x in languages:
#     print(x)

# for+break语句,break 语句用于跳出当前循环体：
# sites = ["Baidu", "Google", "Gunxiaoshi", "Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程!")
#         break
#     print("循环数据 " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")

# break和continue语句及循环中的else子句
# break 语句可以跳出 for 和 while 的循环体。
# 如果你从 for 或 while 循环中终止,break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，
# for letter in 'Gunxiaoshi':  # 第一个实例
#     if letter == 'b':
#         break
#     print('当前字母为 :', letter)
#
# var = 10  # 第二个实例
# while var > 0:
#     print('当期变量值为 :', var)
#     var = var - 1
#     if var == 5:
#         break
# print("Good bye!")


# continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
# for letter in 'Gunxiaoshi':  # 第一个实例
#     if letter == 'o':  # 字母为 o 时跳过输出
#         continue
#     print('当前字母 :', letter)
#
# var = 10  # 第二个实例
# while var > 0:
#     var = var - 1
#     if var == 5:  # 变量为 5 时跳过输出
#         continue
#     print('当前变量值 :', var)
# print("Good bye!")

# pass语句是空语句，是为了占用程序结构的完整性。
# pass不做任何事情，一般用作占位语句
for letter in 'Gunxiaoshi':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")

# 记录生肖，根据年份来判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = int(input("Please user input year:"))