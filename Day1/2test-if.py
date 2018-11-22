#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 16:19
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 2test-if.py
# @Software: PyCharm

# if 判断语句和 if 嵌套语句
# 判断年龄
# age_of_boy = 56  # 不加“”是变量
# guess_age = int(input("guess age:"))
# print("*********************")
# if guess_age < 0:
#     print("You must be teasing me!")
# elif guess_age < age_of_boy:
#     print("think bigger...")
# elif guess_age == age_of_boy:
#     print("Yes,you get  it.")
# elif guess_age > age_of_boy:
#     print("think smaller...")
# # 退出提示
# input("Please enter the Enter key to exit.")

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

# num = int(input("输入一个数字："))
# if num % 2 == 0:
#     if num % 3 == 0:
#         print("你输入的数字可以整除 2 和 3")
#     else:
#         print("你输入的数字可以整除 2，但不能整除 3")
# else:
#     if num % 3 == 0:
#         print("你输入的数字可以整除 3，但不能整除 2")
#     else:
#         print("你输入的数字不能整除 2 和 3")

# 练习：使用if语句判断字符串的长度是否等于10，根据判断结果进行不同的输出
string1 = '123456789'
# 使用len( )可以计算字符串的长度
print(len(string1))

# 判断相等可以使用“==”， 不相等可以使用 not 关键字
if not len(string1) == 10:
    print('字符串长度不为10')
else:
    print('字符串长度为10')

#  提示用户输入一个1-40之间的数字，使用if语句根据输入数字的大小进行判断，如果输入的数字在
num_user_input = input('输入一个1-40之间的整数：')
num_to_int = int(num_user_input)
if 1 <= num_to_int <= 10:
    print('数字在1-10之间')
elif 11 <= num_to_int <= 20:
    print('数字在11-20之间')
elif 21 <= num_to_int <= 30:
    print('数字在21-30之间')
else:
    print('数字在31-40之间')

