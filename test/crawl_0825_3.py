"""
Title:多线程爬虫
Author:kingsley
Version:0.1
Question:从网站获取美女图片的爬虫，用requests获取html，用bs4解析，多线程高效爬取
Preparation:
网址：
http://www.mm288.com/meinv/mnxh/1.html
http://www.mm288.com/meinv/mnxh/2.html
元素：img
"""
import requests
import os
from bs4 import BeautifulSoup as bs


def request_girl(url):
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        # 判断http是否请求成功，成功则返回html数据
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_html(html):
    # 使用html.parser解析，也有lxml解析
    # find是针对html解析，select是针对css解析
    soup = bs(html, 'lxml')
    boxs = soup.find(class_='Clbc_Game_l_b').find_all(class_='item masonry_brick masonry-brick')

    titles = []
    pics = []
    for box in boxs:

        img = box.find('img')
        alt = img.get('alt')
        src = img.get('src')

        # li = soup.find(class_='item mas').find_all('li')
        titles.append(alt)
        pics.append(src)

    return titles, pics


def download_Pic(titles, pics):
    path = 'D:\\2345Downloads\\' + str(titles[0])
    i = 1
    if not os.path.exists(path):
        os.mkdir(path)
    for pic in pics:
        dir = path + '\\' + str(titles[i-1]) + '.jpg'

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
        response = requests.get(pic, headers=headers)
        img = response.content
        print('开始下载：%s' % titles[i-1])
        fp = open(dir, 'wb')
        fp.write(img)
        fp.close()
        i += 1


def main(page):
    """主函数"""
    url = 'http://www.mm288.com/meinv/mnxh/' + str(page) + '.html'
    html = request_girl(url)
    titles, pics = parse_html(html)
    download_Pic(titles, pics)


if __name__ == '__main__':
    for i in range(1, 3):
        main(i)
