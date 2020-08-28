"""
Title:爬虫
Author:kingsley
Version:0.1
Question:从网易体育获取NBA新闻标题和连接的爬虫
"""
import requests
import re
import json


def request_dandan(url):
    try:
        response = requests.get(url)
        # 判断http是否请求成功，成功则返回html数据
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(html):
    pattern = re.compile('<li.*?(\d+).</div>.*?<img src="(.*?)".*?<div class="name".*?title="(.*?)".*?</li>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        # 带有yield的函数就是一个generator，next后自动中断，并返回一个迭代值
        yield {
            'id': item[0],
            'image': item[1],
            'title': item[2]
        }


def write_item_to_file(item):
    with open('D:\\2345Downloads\\book.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()


def main(page):
    """主函数"""
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dandan(url)
    items = parse_result(html)

    for item in items:
        write_item_to_file(item)


if __name__ == '__main__':
    for i in range(1, 26):
        main(i)