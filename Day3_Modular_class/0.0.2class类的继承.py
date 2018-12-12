#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 14:44
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.2class类的继承.py
# @Software: PyCharm


# 猫科动物 ————> 猫
# 面向对象编程中，父类 ——————> 子类，父类中定义好的方法，子类可以继续使用
# 使用的这个过程叫做调用、
# class Player:
#     def __init__(self, name, hp, occu):  # 将变量和实例绑定到一起。
#         self.__name = name
#         self.hp = hp
#         self.occu = occu  # 变量的名称等于传进来的变量，
#
#     def print_role(self):  # 定义一个方法
#         print('%s %s %s' % (self.__name, self.hp, self.occu))
#
#     def updateName(self, newname):
#         self.__name = newname


# 编写类的时候，首先要将类的逻辑关系写好，然后分别实现每个类的属性和方法：
class Monster():
    '定义怪物类'

    def __init__(self, hp=500):
        self.hp = hp

    def run(self):
        print('移动到某个位置')

    # 子类中定义的方法与父类中的方法重名,子类调用的方法会覆盖父类的方法
    def whoami(self):
        print("我是怪物的父类")


class Animals(Monster):
    '普通怪物'

    def __init__(self, hp=10):
        # self.hp = hp
        # # super是直接从父类中找方法，那就需要super()函数了。
        # 在Animals中hp不用再初始化，在父类中已经初始化了
        super().__init__(hp)


class Boss(Monster):
    'Boss类怪物'

    def whoami(self):
        print("我是BOSS我怕谁！")


a1 = Monster(100)  # 关于覆盖的说明，初始化的说明，在定义方法的时候，可以直接赋值如hp = 200,后续可直接覆盖
print(a1.hp)
print(a1.run())
a2 = Animals(1)  # 子类继承父类的run，面向对象的一个特性——继承。
print(a2.hp)
print(a2.run())
a3 = Boss(800)  # 面向对象的另一个特性——多态。
a3.whoami()

# 判断子类父类的方法：
# 判断
print('a1的类型 %s' % type(a1))
print('a2的类型 %s' % type(a2))
print('a3的类型 %s' % type(a3))
# 判断子类的归属
print(isinstance(a3, Monster))
print(isinstance(a3, Animals))

# # 对职业作为参数传递到类中，对user增加属性
# user1 = Player('tom', 100, 'warrior')
# user2 = Player('jerry', 80, 'master')
# user1.print_role()
# user2.print_role()
#
# user1.updateName('wilson')
# user1.print_role()
# user2.__name = 'test'  # 不能通过赋值对类中修改，修改类中的某一个属性的时候只能通过方法去修改
# user2.print_role()  # 增加方法对类修改，称为类的封装


# 面向对象编程，封装、继承、多态，类没有办法直接使用，实例化
