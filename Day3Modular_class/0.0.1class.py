#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 17:59
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.0class.py
# @Software: PyCharm


# 面向过程编程，更适合机器执行
# user1 = {'name': 'tom', 'hp': 100}
# user2 = {'name': 'ferry', 'hp': 80}
#
#
# def print_role(rolename):
#     print('name is %s, hp is %s' % (rolename['name'], rolename['hp']))
#
#
# print_role(user1)
# print_role(user2)


# 面向对象编程，更符合人的习惯
# class是一个关键字，关键字定义一个类，将相似东西进行一定的归纳。
# 列表，元组等都是类

# 定义了一个类,类首字母要大写###
class Player:
    # #类中的函数（方法）的第一个参数一定要带上self ##
    def __init__(self, name, hp):    # 面向对象中，变量被称为属性
        # self表示player这个类实例化之后，这个类的实例化本身
        # self.name和self.hp分别表示userX.name和userX.hp
        self.name = name
        self.hp = hp

    def print_role(self):    # 定义一个方法
        print('%s %s' % (self.name, self.hp))


# 这个过程，变量和类做关联，这样变量就拥有的类的特征
# 类的实例化###
user1 = Player('tom', 100)
user2 = Player('jerry', 80)
user1.print_role()
user2.print_role()

# 实例-> 方法
# 人 -> 动作

#