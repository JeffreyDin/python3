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
var1 = 123

def func():
    # var1 = 456
    global var1
    var1 = 456
    print(var1)

func()
print(var1)
