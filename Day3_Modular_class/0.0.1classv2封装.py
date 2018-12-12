#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 17:59
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.0class.py
# @Software: PyCharm


# 面向对象编程，更符合人的习惯
# class是一个关键字，关键字定义一个类，将相似东西进行一定的归纳。

# 定义了一个类,类首字母要大写###
class Player:
    def __init__(self, name, hp, occu):  # 将变量和实例绑定到一起。
        self.__name = name
        self.hp = hp
        self.occu = occu  # 变量的名称等于传进来的变量，

    def print_role(self):  # 定义一个方法
        print('%s %s %s' % (self.__name, self.hp, self.occu))

    def updateName(self, newname):
        self.__name = newname


class Monster():
    ' 定义怪物类 '
    pass


# 对职业作为参数传递到类中，对user增加属性
user1 = Player('tom', 100, 'warrior')
user2 = Player('jerry', 80, 'master')
user1.print_role()
user2.print_role()

user1.updateName('wilson')
user1.print_role()
user2.__name = 'test'  # 不能通过赋值对类中修改，修改类中的某一个属性的时候只能通过方法去修改
user2.print_role()  # 增加方法对类修改，称为类的封装
