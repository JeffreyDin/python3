#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 14:06
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 1.0.0thread.py
# @Software: PyCharm


import threading
import time
from threading import current_thread


def myThread(arg1, arg2):
    print(current_thread().getName(), 'start')
    print('%s %s' % (arg1, arg2))
    time.sleep(2)
    print(current_thread().getName(), 'stop')


for i in range(1, 10, 2):
    # t1 = myThread(i, i + 1)
    t1 = threading.Thread(target=myThread, args=(i, i + 1))
    t1.start()

print(current_thread().getName(), 'end')
