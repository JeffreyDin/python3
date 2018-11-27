#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 17:27
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 01file_op.py
# @Software: PyCharm

# Python内建函数，文件的基本操作
# 将文件的主要人物记录到文件中
# file1 = open('name.txt', 'w')
# file1.write('诸葛亮')
# file1.close()
#
# file2 = open('name.txt')
# print(file2.read())
# file2.close()
#
# # 增加
# file3 = open('name.txt', 'a')
# file3.write('  刘备')
# file3.close()

# 单行读取
# file4 = open('name.txt')
# print(file4.readline())

# 逐行读取标准写法
# f = open('name.txt')
# line = f.readline()
# print(type(line))
# # 每次读出一行内容，所以，读取时占用内存小，比较适合大文件，该方法返回一个字符串对象。
# while line:
#     print(line)
#     print('==========')
#     line = f.readline()
# f.close()

# f = open('name.txt')
# lines = f.readlines()
# print(type(lines))
# # readlines()方法读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素.但读取大文件会比较占内存。
# for line in  lines:
#     print(line)
# f.close()

# 逐行读取写法
# file5 = open('name.txt')
# for line in file5.readlines():
#     print(line)
#     print('==========')
# while 1:
#     line = file5.readline()
#     if not line:
#         break
#     print(line)

# seek函数
# f = open('name.txt')
# print('当前文件指针的位置 %s' % f.tell())
# print('当前文件读到了一个字符，字符内容是 %s' % f.read(1))
# print('当前文件指针的位置 %s' % f.tell())
# # seek()函数，第一个参数偏移量，第二个函数，0代表文件开头开始偏移；1从当前位置开始偏移；2从文件末尾开始偏移
# f.seek(2, 0)
# print(f.tell())
# print('当前文件指针的位置 %s' % f.tell())
# print('当前文件读到了一个字符，字符内容是 %s' % f.read(1))
# print('当前文件指针的位置 %s' % f.tell())
# f.close()

# 将文件保存到列表中，然后修改内容
# f = open(r'E:\Python\Python-primary\Day1\name.txt', 'w')
# f.write('this \nis no \nhaiku!')
# f.close()
# f = open(r'E:\Python\Python-primary\Day1\name.txt')
# lines = f.readlines()
# f.close()
# lines[1] = 'isn`t a\n'
# f = open(r'E:\Python\Python-primary\Day1\name.txt', 'w')
# f.writelines(lines)
# f.close()




