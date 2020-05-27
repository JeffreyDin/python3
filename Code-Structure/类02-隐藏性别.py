#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 17:26
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 类02-隐藏性别.py
# @Software: PyCharm


# 访问限制
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender in ('male', 'female'):
            self.__gender = gender
        else:
            raise ValueError('illegal gender')


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')