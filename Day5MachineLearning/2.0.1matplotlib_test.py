#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 22:09
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 2.0.1matplotlib_test.py
# @Software: PyCharm


# # 绘制散点图
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
#
# iris = pd.read_csv('./iris_training.csv')
# print(iris.head())
#
# iris.plot(kind="scatter", x="120",y="4")
# plt.show()

# 绘制散点图
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
iris = pd.read_csv('./iris_training.csv')
# # 设置样式
sns.set(style="white", color_codes=True)
# # 设置绘制格式为散点图
# sns.jointplot(x="120", y="4", data=iris, size=5)
# # distplot绘制曲线
# sns.distplot(iris['120'])
# plt.show()

# FacetGrid 一般绘图函数
# hue 彩色显示分类0/1/2
# plt.
# add_legend()显示分类的描述信息scatter绘制散点图
# sns.FacetGrid(iris, hue='virginica', size=5).map(plt.scatter, '120', '4').add_legend()
sns.FacetGrid(iris, hue='virginica', size=5).map(plt.scatter, 'setosa', 'versicolor').add_legend()
plt.show()
