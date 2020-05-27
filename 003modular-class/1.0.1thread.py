#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 14:20
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 1.0.1thread.py
# @Software: PyCharm


import threading
from threading import current_thread


class Mythread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')


t1 = Mythread()
t1.start()
t1.join()

print(current_thread().getName(), 'end')