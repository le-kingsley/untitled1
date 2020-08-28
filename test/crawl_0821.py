"""
Title:爬虫
Author:kingsley
Version:0.1
Question:从当当网获取500个图书数据的爬虫，用requests获取html，用bs4解析
"""
import requests
import re
import json
from bs4 import BeautifulSoup as bs

def request_dandan(url):
    try:
        response = requests.get(url)
        # 判断http是否请求成功，成功则返回html数据
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(html):
    # 使用html.parser解析，也有lxml解析
    # find是针对html解析，select是针对css解析
    soup = bs(html, 'html.parser')
    # div = soup.find_all('head')

    ids = soup.find_all('div', class_='list_num')
    names = soup.find_all('div', class_='name')
    s1=[]
    s2=[]
    for j in ids:
        s1.append(j.get_text())
    print(s1)
    for i in names:
        s2.append(i.get_text())
    tmps = dict(zip(s1, s2))
    print(s2)


# def write_item_to_file(item):
#     with open('D:\\2345Downloads\\book.txt', 'a', encoding='UTF-8') as f:
#         f.write(json.dumps(item, ensure_ascii=False) + '\n')
#         f.close()


def main(page):
    """主函数"""
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dandan(url)
    parse_result(html)

    # for item in items:
    #     write_item_to_file(item)
    #     print(item)

if __name__ == '__main__':
    for i in range(1, 3):
        main(i)