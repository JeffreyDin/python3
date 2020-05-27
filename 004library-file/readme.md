# 日常应用比较广泛的模块是：
 * 1.文字处理的 re
 * 2.日期类型的time、datetime
 * 3.数字和数学类型的math、random
 * 4.文件和目录访问的pathlib、os.path
 * 5.数据压缩和归档的tarfile
 * 6.通用操作系统的os、logging、argparse
 * 7.多线程的 threading、queue
 * 8.Internet数据处理的 base64 、json、urllib
 * 9.结构化标记处理工具的 html、xml
 * 10.开发工具的unitest
 * 11.调试工具的 timeit
 * 12.软件包发布的venv
 * 13.运行服务的__main__
----

# word excel pdf
word excel pdf 都有专门处理的库，一般在处理陌生格式的文档时也是通过搜索引擎现用现查的。
比如excel使用xlrd和xlwt库，也可以使用openpyxl库，要看哪个功能更符合你期望的需求。甚至有时候为了简化库的使用，先做格式转换，例如将excel先转换为csv，可以直接用文本方式处理了。
拆CSV文件
# web开发
可以关注flask、django框架的编写。
# 机器学习
可以关注tensorflow库的编写等等。
# 数据库
在Python中连接数据库方式可以分为数据库接口和ORM方式 

数据库接口方式访问关系型数据库，如MySQL可以使用MySQLdb，MySQL，Oracle数据库使用Oracle包，使用pip安装即可 
非关系型数据库，如MongoDB，可以使用pyMongo3、MongoDB包 
需要去熟悉各种包的用法，掌握连接方式，他们的操作方式统一是使用SQL语句方式 

另一种连接数据库方式是ORM方式，使用ORM方式不用显式的给出SQL命令，将SQL语句抽象成对象。如Django Web框架连接数据库就使用了ORM方式。 

建议参考资料 《Python官方文档》《Django官方文档》《Python核心编程》
# 运维工程师
能自动化或者半自动化你的变更，能用python解决重复性的工作，能用web方式展示和操作你的系统更佳。
配置文件操作会需要re、jinja2库做文本替换，对文件目录操作的os、shutil、tarfile库，处理交互模式的pexpect、paramiko库，集中化管理的ansible库，web框架django、flask库等等

# python爬虫框架
## python爬虫框架非常多，比较流行主要有Scrapy、PySpider
_Scrapy，有XPath和CSS选择器，个人使用习惯更好用一些_
据使用过两个爬虫框架的人说，pyspider更简单，上手较快，其他区别可以通过搜索引擎进行比较。
还有值得学习的有urllib2、urllib3、selenium这些包，简单的爬虫用urllib就可以实现了
selenium可以调用浏览器，完整的解析js，当然执行速度上要慢，这些都是编写爬虫常用的包
