#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Farr Ding  Time: 2018/6/11

'''age_of_oldboy = 56

guess_age = int(input("guess age:"))

if guess_age == age_of_oldboy:
    print("yes, you get it.")
elif guess_age > age_of_oldboy:
    print("think smaller...")
else:
    print("think bigger...")

'''


age_of_oldbay = 56   #不加“”是变量
count = 0
while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldbay:
        print("Yes,you get it.")
        break
    elif guess_age > age_of_oldbay:
        print("think smaller...")
    else:
        print("think bigger...")
    count += 1

#if count == 3:
else:
    print("you have tried too many times...fuck off")
