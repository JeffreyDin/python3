#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 11:41
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.2.1.py
# @Software: PyCharm


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 格式化代码 {0.x} 对应的是第1个参数的x属性。 因此，在下面的函数中，0实际上指的就是 self 本身
    # def __repr__(self):
    #     return 'Pair({0.x!r}, {0.y!r})'.format(self)

    # 作为这种实现的一个替代，你也可以使用 % 操作符，就像下面这样：
    def __repr__(self):
        return 'Pair(%r, %r)' % (self.x, self.y)

    # '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


# __repr__() 方法返回一个实例的代码表示形式，通常用来重新构造这个实例。
# 内置的 repr() 函数返回这个字符串，跟我们使用交互式解释器显示的值是一样的。
# __str__() 方法将实例转换为一个字符串
# 使用 str() 或 print() 函数会输出这个字符串。
p = Pair(3, 4)
# >>> p
# Pair(3, 4) # __repr__() output
# >>> print(p)
# (3, 4) # __str__() output
print(p)
print(str(p))
print(repr(p))
print('----------------------')

# # !r 格式化代码指明输出使用 __repr__() 来代替默认的 __str__()
p2 = Pair(5, 6)
print('p is {0!r}'.format(p2))
# p is Pair(3, 4)
print('p is {0}'.format(p2))
# p is (3, 4)
print('p is {0!s}'.format(p2))
# p is (3, 4)
