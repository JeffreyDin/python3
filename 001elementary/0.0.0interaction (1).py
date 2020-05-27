#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Farr Ding  Time: 2018/6/11

# raw_input 2.x    input 3.x
# input 2.x   输入是什么格式，输出就是什么格式；直接输入，会被当成变量，想输入字符串，必须加""
name = input("Name:")
age = int(input("Age:"))  #integer
print(type(age), type(str(age)), )
job = input("Job:")
salary = input("Salary:")

# info0 = '''
# ------------ info of ''' + name +''' -------------
# Name:'''+ age +'''
# Age:'''+ job +'''
# Job:'''+ salary +'''
# Salary:'''+ salary


info = '''
------------ info of %s -------------
Name:%s
Age:%d
Job:%s
Salary:%s
''' % (name, name, age, job, salary)

print(info)
