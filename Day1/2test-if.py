#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 16:19
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 2test-if.py
# @Software: PyCharm

# if 判断语句和 if 嵌套语句
# 判断年龄
age_of_boy = 56  # 不加“”是变量
guess_age = int(input("guess age:"))
print("*********************")
if guess_age < 0:
    print("You must be teasing me!")
elif guess_age < age_of_boy:
    print("think bigger...")
elif guess_age == age_of_boy:
    print("Yes,you get  it.")
elif guess_age > age_of_boy:
    print("think smaller...")
# 退出提示
input("Please enter the Enter key to exit.")

# if 语句嵌套
# if 表达式1:
#     语句
#     if 表达式2:
#         语句
#     elif 表达式3:
#         语句
#     else:
#         语句
# elif 表达式4:
#     语句
# else:
#     语句

num = int(input("输入一个数字："))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除 2 和 3")
    else:
        print("你输入的数字可以整除 2，但不能整除 3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除 3，但不能整除 2")
    else:
        print("你输入的数字不能整除 2 和 3")