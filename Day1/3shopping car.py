#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 16:10
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 3shipping car.py
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
            # print(Product_list.index(item), item)
        # 打印商品列表，取出下标
        for index, item in enumerate(Product_list):
            # 每次循环留两个值，下标和数据
            print(index, item)
        user_choice = input("Please choose goods>>>:")

        if user_choice.isdigit():
            # 　判断用户的输入是否为数字类型
            user_choice = int(user_choice)
            if user_choice < len(Product_list) and user_choice >= 0:
                # 判断用户输入的编号是否小于或等于商品编号
                p_item = Product_list[user_choice]
                # 通过下标把商品取出来
                if p_item[1] <= salary:   # 买得起
                    # 加入购物车
                    Shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart, "
                          "your current balance is \033[32;1m%s\033[0m" % (p_item, salary))
                                 # 红色31，绿色32
                else:
                    print("\033[41m你的余额只剩[%s]啦，还买个毛线啊！\033[m" % salary)
            else:
                print("\033[42mProduct code [%s] is not exist!\033[m" % user_choice)
        elif user_choice == 'q':
            print("------shopping list------")
            for p in Shopping_list:
                print(p)
            print("Your current balance:", salary)
            exit()
        else:
            print('invalid option!')

