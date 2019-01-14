#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 17:41
# @Author  : Jianfeng Ding
# @Site    :
# @File    : 0.0.5装饰器.py
# @Software: PyCharm

# time函数
# # sleep
# import time
#
# print(time.time())
#
#
# # time.sleep(3)
# def i_can_sleep():
#     time.sleep(3)
#
#
# # 统计函数运行时间
# start_time = time.time()
# i_can_sleep()
# stop_time = time.time()
# print('函数运行 %s 秒' % (stop_time - start_time))

# # 装饰器,将重复多次的事情只做一次
import time


def timer(func):
    def wrapper():
        start_time = time.time()  # 额外功能1
        func()
        stop_time = time.time()  # 额外功能２
        print("运行时间是 %s 秒" % (stop_time - start_time))  # 额外功能３

    return wrapper


# # @timer 语法糖
@timer
# timer(计时器)是装饰器的装饰函数，i_can_sleep是被装饰函数
# 装饰函数和被装饰函数写好后，那么额外的功能就可以写到装饰函数里
def i_can_sleep():
    time.sleep(3)


i_can_sleep()
# 使用装饰器之后，可以直接用i_can_sleep()函数，不用再写上面的功能1，2，3
# num = timer(i_can_sleep)
# num()
# num**的方式不简单优雅，逐渐演化成i_can***


# 使用装饰器后，程序的执行过程：
# 调用函数:i_can_sleep(),发现语法糖@timer，调用timer()函数，
# 将i_can_sleep()传递进去，变成timer(i_can_sleep())，
# 看timer()函数,定义func函数，定义内部函数wrapper()，引用func(),返回wrapper


# 装饰器与闭包的区别
# 装饰器传递进来的是函数,内部引用的也是函数;闭包传递进来的变量,内部引用的也是变量;
