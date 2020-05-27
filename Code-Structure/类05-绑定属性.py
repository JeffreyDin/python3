#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 10:56
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 类04-学生人数.py
# @Software: PyCharm


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


class GraduateStudent(Student):
    pass


s = Student()        # 创建新的实例
s.name = 'Michael'   # 绑定属性'name'
s.age = 25           # 绑定属性'age'
print('s.name =', s.name)
print('s.age =', s.age)

# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)
