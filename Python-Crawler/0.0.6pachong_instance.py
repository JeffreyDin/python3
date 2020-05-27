#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 19:35
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.2pachong_http_headers.py
# @Software: VSCode


from bs4 import BeautifulSoup
import requests

# 伪装成合法的浏览器
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; "
              "_gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.light2cloud.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, sdch",
#     "Accept-Language": "zh-CN,zh;q=0.8",
#     "Connection": "close",
#     "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; "
#               "_gauges_unique_year=1; _gauges_unique=1",
#     "Referer": "http://news.sina.com.cn/china/",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
# }

# 定义请求路径
url = 'http://www.light2cloud.com/'


# 取得新闻标题
def craw2(url):
    response = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    for title_href in soup.find_all('div', class_='main'):
        for class1 in title_href.find_all('p'):
            print(class1)
            for class2 in class1.find_all('class'):
                print(class2)
                print("---------------")
                if class1.get('test'):
                    print(class1.get('test') + '滚小石')
                    print("滚小石")
        # print([title.get('test')for title in title_href.find_all('a') if title.get('test')])


craw2(url)
print(type(url))

# 翻页
# for i in range(15, 46, 15):
#     url = 'http://www.light2cloud.com/' + str(i)
#     # print(url)
#     craw2(url)
