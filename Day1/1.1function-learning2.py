#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 15:17
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 00function-learning2.py
# @Software: PyCharm

name = input("Name:")
age = int(input("Age:"))  # integer
print(type(age), type(str(age)), )
job = input("Job:")
salary = input("Salary:")
info = '''
------------infoof%s-------------
Name:%s
Age:%d
Job:%s
Salary:%s
''' % (name, name, age, job, salary)
print(info)

info3 = '''
------------infoof{0}-------------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name, age, job, salary)
print(info3)




