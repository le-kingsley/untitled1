"""
Title:crawl大众点评
Author:kingsley
Version:0.1
Question:大众点评，获取坐标偏移的文字字典
"""

import requests
from bs4 import BeautifulSoup
import re

class TiebaSpider():
    # 一个贴吧爬取类处理
    def __init__(self, url):
        self.__url = url
        self.__headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }
        pass

    def get_url_list(self):
        pass

    def get_content(self, url):
        req = requests.get(url=url, headers=self.__headers)
        html = req.content
        return html

    def get_items(self, html):
        soup = BeautifulSoup(html, 'lxml')
        texts = []
        for link in soup.findAll('a'):
            t = re.match('https//read(.*)', link.get('href'))
            print(t)
        return texts

    def save_items(self, items):
        pass

    def run(self):
        content = self.get_content(url)
        text = self.get_items(content)
        print(text)

if __name__ == '__main__':
    # 输入所要查询网址url及小说名称
    # url = 'https://www.qidian.com/search?kw=' + '赏金猎手'
    url = 'https://book.qidian.com/info/1019500511#Catalog'
    spider = TiebaSpider(url)
    spider.run()

