"""
网络爬虫即网络数据采集
应用领域：搜索引擎，新闻聚合，社交应用，舆情监控，行业数据

HTTP：超文本传输协议，在网页上的内容通常是浏览器执行HTML语言得到的结果，HTTP就是传输HTML数据的协议。
网站有自身的robots.txt和Sitemap文件
获取作者，python-whois

简单基本流程：数据采集，数据处理，数据存储
优化：采集和处理时使用并发编程或分布式技术

为了爬取网页内容，使用的方法需要适合网站的结构
1.如何安全的下载网站
2.爬取（爬取网站地图，遍历每个网页的数据库id，跟踪网页链接）
下载网站方法：urllib下载网页，需要read().decode() 读取并解码
解析网站地图：使用正则表达式从<loc>标签中提取出URL，后面用CSS选择器

爬取网站数据方法：正则表达式，BeautifulSoup，lxml
"""
from urllib import request
from urllib import parse
from urllib import robotparser
import urllib
import urllib.error
import re
import itertools
import time
from datetime import datetime
import lxml.html

def download(url, user_agent= 'wswp', proxy= None, num_retries = 2):
    print('Downloading', url)
    headers = {'User-agent': user_agent}
    request = urllib.request.Request(url, headers= headers)

    opener = urllib.request.build_opener()
    if proxy:
        proxy_params = {urllib.parse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))
    try:
        html = urllib.request.urlopen(url).read().decode('utf-8')
    except urllib.error.URLError as e:
        print('Download error', e.reason)
        html = None
        if num_retries> 0:
            if hasattr(e, 'code') and 500<= e.code< 600:
                return download(url, num_retries-1)
    return html

def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    for link in links:
        html= download(url)
def id_crawler(url):
    #id遍历爬虫
    max_error= 5
    num_error= 0
    for page in itertools.count(1):
        url= 'http://example.webscraping.com/view/-%d' % page
        html= download(url)
        if html is None:
            num_error+= 1
            if max_error== num_error:
                break
        else:
            num_error= 0

def link_crawler(seed_url, link_regex):
    #链接爬虫
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urllib.parse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)

def main():
    # download('http://example.webscraping.com/sitemap.xml')
    # crawl_sitemap('http://example.webscraping.com/sitemap.xml')
    # seed_url = 'http://example.webscraping.com/index'
    # link_regex = '/(index|view)'
    # link_crawler(seed_url, link_regex)
    broken_html = '<ul class= country><li>Area<li>Population</ul>'
    tree = lxml.html.fromstring(html)
    td = tree.cs
    fixed_html = lxml.html.tostring(tree, pretty_print=True)
    print(fixed_html)


if __name__ == '__main__':
    main()