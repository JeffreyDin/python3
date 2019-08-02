#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 10:54
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.0func函数变量作用域.py
# @Software: PyCharm

# 简单说，函数变量作用域，函数内部某变量与外部某变量同名
# 若内部没有赋值，同名变量指定为外部变量的值
# 若内部赋值，覆盖外部同名变量的值，作用于缩进部分
# 若内部赋值，成为全局变量,添加关键字
# var1 = 123
#
#
# def func():
#     # var1 = 456
#     # global var1
#     var1 = 456
#     print('nei:', var1)
#
#
# func()
# print(var1)

# name = "Alex Li"   # 全局变量
#
# def change_name(name):
#     print("before change:",name) # 函数内部变量从内向外找，如果内部不存在，会找上一层
#     # 输出
#     # before change: Alex Li
#     name = "金角大王,一个有Tesla的男人" #局部变量
#     print("after change", name)
#     # 输出
#     # after change 金角大王,一个有Tesla的男人
#
# change_name(name)
#
# print("在外面看看name改了么?",name)  # 默认局部变量不能修改全局变量的值

name = "Alex Li"


def change_name():
    name = "金角大王,一个有Tesla的男人"
    print("after change", name)
    # 输出
    # after change 金角大王,一个有Tesla的男人

change_name()

print("在外面看看name改了么?", name )