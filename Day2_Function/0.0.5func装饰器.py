#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 17:41
# @Author  : Jianfeng Ding
# @Site    :
# @File    : 0.0.5装饰器.py
# @Software: PyCharm

# time函数
# sleep
# import time
# print(time.time())
# # time.sleep(3)
#
#
# def i_can_sleep():
#     time.sleep(3)
#
#
# # 统计函数运行时间
# start_time = time.time()
# i_can_sleep()
# stop_time = time.time()
# print('函数运行 %s 秒' %(stop_time - start_time))


# 装饰器
import time


def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("运行时间是 %s 秒" % (stop_time - start_time))

    return wrapper


# ######语法糖
@timer
# 计时器  （装饰函数）
def i_can_sleep():
    time.sleep(3)


i_can_sleep()
# num = timer(i_can_sleep)
# num()
# num**的方式不简单优雅，逐渐演化成i_can***
