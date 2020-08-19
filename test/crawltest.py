"""
Title:crawl
Author:kingsley
Version:0.1
Question:爬虫程序一般通过模拟浏览器对相应的URL发送请求，获取数据，
并通过正则等匹配手段配出页面中需要的信息
"""
import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    # 获取文件内容
    path = 'D:\\example.html'
    file = open(path, 'r', encoding='utf-8')
    htmlhandle = file.read()
    # 加载html文件，第一个参数是html句柄内容，不是html文件，所以把文件内容读取，并赋值
    soup = BeautifulSoup(htmlhandle, 'html.parser')
    tmp = soup.find_all('div')
    print(tmp)
    li = soup.find_all('li')
    print(li)
    for i in li:
        print(i.text)
