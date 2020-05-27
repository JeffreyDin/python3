#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 10:49
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.3class_with.py
# @Software: PyCharm


class Testwith():
    # 类在初始化和结束的时候会被调用到
    def __enter__(self):
        print('run')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('正常结束')
        else:
            print('It has error %s' % exc_tb)


with Testwith():
    print('test is running')
    raise NameError('testNameError!')
