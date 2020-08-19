"""
Title:crawltest
Author:kingsley
Version:0.1
Question:爬取网站小说，并存到txt文件中
"""
from datetime import datetime
import requests
from bs4 import BeautifulSoup

"""
小说下载类
"""
def get_content(url):
    req = requests.get(url)
    req.encoding = 'utf-8'
    html = req.text
    bfs = BeautifulSoup(html, 'lxml')
    texts = bfs.find('div', id='content')
    content = texts.text.strip().split('\xa0'*4)
    return content


if __name__ == '__main__':
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('\n\t\t欢迎使用《笔趣小说网》免费看小说\n\n\t作者：kingsley\t时间：{}'.format(date))
    print('************************************************')
    server = 'https://www.xsbiquge.com'
    book_name = 'D:\\诡秘之主.txt'
    target = 'https://www.xsbiquge.com/15_15338/'
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'lxml')
    chapters = chapter_bs.find('div', id='list')
    chapters = chapters.find_all('a')
    for chapter in chapters:
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')
