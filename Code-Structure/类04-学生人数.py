#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 10:56
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 类04-学生人数.py
# @Software: PyCharm


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')