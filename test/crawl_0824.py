"""
Title:爬虫
Author:kingsley
Version:0.1
Question:从豆瓣网获取250个电影数据的爬虫，用requests获取html，用bs4解析
Preparation:
豆瓣25页：https://movie.douban.com/top250
豆瓣50页：https://movie.douban.com/top250?start=25&filter=
豆瓣75页：https://movie.douban.com/top250?start=50&filter=
提取数据类型：电影名称、电影图片、电影排名、电影评分、电影作者、电影简介
            title,    pic,     em,      rating_num, p,    p class=quote
此项目表示bs4不使用html.parser 而用lxml，结果相同
"""
import requests
from bs4 import BeautifulSoup as bs
import re
import json
import xlwt  # excel操作库


def request_douban(url):
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=3)
        # 判断http是否请求成功，成功则返回html数据
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


# excel存储
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
sheet.write(0, 0, '电影排名')
sheet.write(0, 1, '电影名称')
sheet.write(0, 2, '电影图片')
sheet.write(0, 3, '电影评分')
sheet.write(0, 4, '电影作者')
sheet.write(0, 5, '电影简介')

n=1


def parse_save_to_excel(html):
    # 使用html.parser解析，也有lxml解析
    # find是针对html解析，select是针对css解析
    soup = bs(html, 'lxml')
    li = soup.find(class_='grid_view').find_all('li')
    items = []
    for i in li:
        # 电影排名
        index = i.find('em', class_='').string
        # 电影名称
        name = i.find('span', class_='title').string
        # 电影图片
        img = i.find('div', class_='pic').find('img').get('src')
        # 电影评分
        score = i.find('span', class_='rating_num').string
        # 电影作者
        author = i.find('p').text
        author = author.strip().replace('\n', '')
        # 电影简介
        # 此处加判断，排除
        if (i.find('span', class_='inq') != None):
            intr = i.find('span', class_='inq').string
        # 用字典封装
        dict = {
            'index': index,
            'name': name,
            'img': img,
            'score': score,
            'author': author,
            'intr': intr
        }
        items.append(dict)

        # 数据写入excel表
        global n
        sheet.write(n, 0, index)
        sheet.write(n, 1, name)
        sheet.write(n, 2, img)
        sheet.write(n, 3, score)
        sheet.write(n, 4, author)
        sheet.write(n, 5, intr)
        n = n + 1

    return items


def main(page):
    """主函数"""
    url = 'https://movie.douban.com/top250?start=' + str(page * 25) + '&filter='
    html = request_douban(url)
    items = parse_save_to_excel(html)
    for item in items:
        print(item)


if __name__ == '__main__':
    for i in range(0, 10):
        main(i)

book.save('D:\\2345Downloads\\豆瓣最受欢迎的250部电影-lxml.xls')
