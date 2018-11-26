#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 16:16
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 3shopping car learning.py
# @Software: PyCharm

Product_list = [
    ('IPhone', 6000),
    ('Mac Pro', 12000),
    ('Starbucks Latte', 50),
    ('Beginning python', 79),
    ('Bicycle', 800),
    ('Watches', 1200)
]

Shopping_list = []

salary = input("Input your salary:")
# 输入工资，判断工资是否为数字,如果是数字，则int
if salary.isdigit():
    salary = int(salary)
    while True:
        # for item in Product_list:
        #     print(Product_list.index(item), item)
        # # 打印商品列表，取出下标,index() 方法检测字符串中是否包含子字符串 str
        # break

        # #  enumerate()函数取出元素下标
        for index, item in enumerate(Product_list):
            print(index, item)
        user_choice = input("Please choose goods>>>:")

        if user_choice.isdigit():
            # 　判断用户的输入是否为数字类型
            user_choice = int(user_choice)
            # 判断用户输入的编号是否小于或等于商品编号
            if user_choice < len(Product_list) and user_choice >= 0:
                # 通过下标把商品取出来
                p_item = Product_list[user_choice]

                if p_item[1] <= salary:   # 买得起
                    # 加入购物车
                    Shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart, "
                          "your current balance is \033[32;1m%s\033[0m" % (p_item, salary))
                                 # 红色31，绿色32
                else:
                    print("\033[41m你的余额只剩[%s]啦，还买个毛线啊！\033[m" % salary)