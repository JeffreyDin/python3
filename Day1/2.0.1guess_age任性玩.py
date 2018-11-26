#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Farr Ding  Time: 2018/6/12

age_of_oldboy = 56
count = 0
while count<3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("Yes,you get it!")
        break
    elif guess_age > age_of_oldboy:
        print("guess smaller...")
    else:
        print("guess bigger...")
    count +=1
    if count ==3:
        countine_confirm = input("Do you want to keep guessing?")
        if countine_confirm != 'n':
            count = 0



