#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Farr Ding  Time: 2018/6/12

age_of_oldbay = 56   #不加“”是变量
for i in range(3):
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldbay:
        print("Yes,you get it.")
        break
    elif guess_age > age_of_oldbay:
        print("think smaller...")
    else:
        print("think bigger...")

#if count == 3:
else:
    print("you have tried too many times...fuck off")