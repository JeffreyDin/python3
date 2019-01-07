#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 17:44
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 2.0.0matplotlib_test.py
# @Software: PyCharm

import matplotlib.pyplot as plt

# 绘制简单的曲线
# plt.plot([1, 3, 5], [4, 8, 10])
# plt.show()

import numpy as np

# # x轴的定义域为 -3.14~3.14，中间间隔100个元素;
# # np.linspace直线
# x = np.linspace(-np.pi, np.pi, 100)
# # y轴纵坐标sin(x)
# plt.plot(x, np.sin(x))
# # 显示所画的图
# plt.show()

# x = np.linspace(-np.pi * 2, np.pi * 2, 100)
# # 创建图表，精度是100，dpi越高，体积越大，越清晰
# plt.figure(1, dpi=100)
# # 绘制4条线
# for i in range(1, 5):
#     plt.plot(x, np.sin(x / i))
# plt.show()


# 直方图
# plt.figure(1, dpi=100)
# data = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 4]
# plt.hist(data)  # 只要写入数据，直方图就会统计数据出现的次数
# plt.show()


# 散点图
x = np.arange(1, 10)
y = x
fig = plt.figure()
# c='r'散点颜色为红色, marker='o'指定散点多形状为圆形。s方形
plt.scatter(x, y, c='g', marker='o')
plt.show()


#