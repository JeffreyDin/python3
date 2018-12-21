#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 16:28
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.0regular.py
# @Software: PyCharm

# 日常应用比较广泛的模块是：
# 1. 文字处理的 re
# 2. 日期类型的time、datetime
# 3. 数字和数学类型的math、random
# 4. 文件和目录访问的pathlib、os.path
# 5. 数据压缩和归档的tarfile
# 6. 通用操作系统的os、logging、argparse
# 7. 多线程的 threading、queue
# 8. Internet数据处理的 base64 、json、urllib
# 9. 结构化标记处理工具的 html、xml
# 10. 开发工具的unitest
# 11. 调试工具的 timeit
# 12. 软件包发布的venv
# 13. 运行服务的__main__

# . 匹配任意的单个字符
# ^ $
# * 匹配前面的字符出现0次或多次
# + ? {m}
# {m, n}　　出现m~n次
#  [] | \d \D \s ()
# ^$   空行
# .*?  非贪婪模式
# abccccccccd
# # abc*  ->  abcccccccc
# # abc*?  ->  ab
#
import re
# compile 匹配的字符串
# match　要匹配的字符串
p = re.compile('cat*?')
print(p.match('catttttttttd'))

# c[abcd]t
# cat
# cbt
# cct
# cdt

# [0-9]+        \d  表示数字
# 123-456-789   \D  表示不包括数字
# ()   表示分组

import re

# p = re.compile('.{3}')
# print(p.match('lennnnn'))

# # p = re.compile('....-..-..')
# p = re.compile('(\d+)-(\d+)-(\d+)')
# print(p.match('2018-05-10'))
# print(p.match('2018-05-10').group(2))
# print(p.match('2018-05-10').groups())
# # 取出,并赋值
# year, month, day = p.match('2018-05-10').groups()
# print(year)