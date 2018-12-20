#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 14:43
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 1.0.2thread_con_cus.py
# @Software: PyCharm

# 多个生产者和多个消费者并行生产和消费
from threading import Thread, current_thread
import time
import random
from queue import Queue

queue = Queue(5)


class ProducerThread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('生产者 %s 生产了数据 %s' % (name, num))
            t = random.randint(1, 3)
            time.sleep(t)
            print('生产者 %s 睡眠了 %s 秒' % (name, t))


class ConsumerTheard(Thread):
    def run(self):
        name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print('消费者 %s 消耗了数据 %s' % (name, num))
            t = random.randint(1, 5)
            time.sleep(t)
            print('消费者 %s 睡眠了 %s 秒' % (name, t))


p1 = ProducerThread(name='p1')
p1.start()
p2 = ProducerThread(name='p2')
p2.start()
p3 = ProducerThread(name='p3')
p3.start()
c1 = ConsumerTheard(name='c1')
c1.start()
c2 = ConsumerTheard(name='c2')
c2.start()
