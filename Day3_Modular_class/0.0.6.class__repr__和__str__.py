#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 11:41
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.2.1.py
# @Software: PyCharm


class Test(object):
    def __init__(self, value='hello, world!'):
        self.data = value


# 重构__repr__
class TestRepr(Test):
    def __repr__(self):
        return 'TestRepr(%s)' % self.data


# 重构__str__
class TestStr(Test):
    def __str__(self):
        return '[Value: %s]' % self.data


# >>> t = Test()
# >>> t
# <__main__.Test at 0x7fa91c307190>
# >>> print t
# <__main__.Test object at 0x7fa91c307190>
# 上面打印类对象并不是很友好，显示的是对象的内存地址
# 重构下该类的__repr__以及__str__，看看它们俩有啥区别
t = Test()
print(t)
# <__main__.Test object at 0x0000025A738E8470>

# >>> tr = TestRepr()
# >>> tr
# TestRepr(hello, world!)
# >>> print tr
# TestRepr(hello, world!)
# 重构__repr__方法后，不管直接输出对象还是通过print打印的信息都按我们__repr__方法中定义的格式进行显示了
tr = TestRepr()
print(tr)
# TestRepr(hello, world!)

# >>> ts = TestStr()
# >>> ts
# <__main__.TestStr at 0x7fa91c314e50>
# >>> print ts
# [Value: hello, world!]
# 直接输出对象ts时并没有按我们__str__方法中定义的格式进行输出，而用print输出的信息却改变了
ts = TestStr()
print(str(ts))
print(ts)
# [Value: hello, world!]
