#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 18:46
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 3.0.1os.py.py
# @Software: PyCharm

import os

# 该文件所在位置：E:\第1层\第2层\第3层\第4层\第5层\test11.py

path1 = os.path.dirname(__file__)
print(path1)  # 获取当前运行脚本的绝对路径

path2 = os.path.dirname(os.path.dirname(__file__))
print(path2)  # 获取当前运行脚本的绝对路径（去掉最后一个路径）

path3 = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(path3)  # 获取当前运行脚本的绝对路径（去掉最后2个路径）

path4 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print(path4)  # 获取当前运行脚本的绝对路径（去掉最后3个路径）

path5 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
print(path5)  # 获取当前运行脚本的绝对路径（去掉最后4个路径）

path6 = os.__file__  # 获取os所在的目录
print(path6)
print('-------------')

# 结合os.path.abspath用，一些python架构的代码实例: os.path.abspath(__file__)返回的是.py文件的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

print(SQLALCHEMY_DATABASE_URI)
print(SQLALCHEMY_MIGRATE_REPO)




