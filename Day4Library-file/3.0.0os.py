#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 14:58
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 3.0.0os.py
# @Software: PyCharm

# Python的os模块封装了操作系统的目录和文件操作，
# 要注意这些函数有的在os模块中，有的在os.path模块中。
import os

print(os.path.abspath('.'))


# os.name
# # 'posix'
# # 操作系统类型
# # 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# os.uname()
# #posix.uname_result(sysname='Darwin',
#                    nodename='MichaelMacPro.local',
#                    release='14.3.0',
#                    version='Darwin Kernel Version 14.3.0: ...',
#                    machine='x86_64')
#
# # 要获取详细的系统信息，可以调用uname()函数：
#
# # 在操作系统中定义的环境变量，全部保存在os.environ这个变量中
# os.environ
# # environ({ichael', 'USER': 'michael', 'PATH' ...})
#
# os.environ.get('PATH')
# #'/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin'
# os.environ.get('x', 'default')
# #'default'
# # 要获取某个环境变量的值，可以调用os.environ.get('key')：
#
# # 查看当前目录的绝对路径:
# >>> os.path.abspath('.')
# '/Users/michael'
# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# >>> os.path.join('/Users/michael', 'testdir')
# '/Users/michael/testdir'
# # 然后创建一个目录:
# >>> os.mkdir('/Users/michael/testdir')
# # 删掉一个目录:
# >>> os.rmdir('/Users/michael/testdir')
#
# #把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# # 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# part-1/part-2
#
# # 而Windows下会返回这样的字符串：
# part-1\part-2
#
# #同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
# #  这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
# >>> os.path.split('/Users/michael/testdir/file.txt')
# ('/Users/michael/testdir', 'file.txt')
# # os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
#
# >>> os.path.splitext('/path/to/file.txt')
# ('/path/to/file', '.txt')
# # 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
#
# # 文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
#
# # 对文件重命名:
# >>> os.rename('test.txt', 'test.py')
# # 删掉文件:
# >>> os.remove('test.py')
