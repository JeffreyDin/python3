#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 8:52
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 类4-animal.py
# @Software: PyCharm


# 获取对象信息

# 判断对象类型，使用type()函数
# type()
print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))

import types
print('type(\'abc\')==str?', type('abc')==str)

# 对于class的继承关系来说，使用type()就很不方便
# 要判断class的类型，可以使用isinstance()函数
# 能用type()判断的基本类型也可以用isinstance()判断
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

# 要获得一个对象的所有属性和方法，可以使用dir()函数

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# >>> len('ABC')
# 3
# >>> 'ABC'.__len__()
# 3

# >>> class MyDog(object):
# ...     def __len__(self):
# ...         return 100
# ...
# >>> dog = MyDog()
# >>> len(dog)
# 100

# 仅仅把属性和方法列出来是不够的，
# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))  # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y'))  # 获取属性'y'
print('obj.y =', obj.y)                            # 获取属性'y'

print('getattr(obj, \'z\') =', getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404

f = getattr(obj, 'power')                               # 获取属性'power'
print(f)
print(f())                # 调用fn()与调用obj.power()是一样的
print(obj.power())
