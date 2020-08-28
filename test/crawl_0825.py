"""
Title:爬虫
Author:kingsley
Version:0.1
Question:selenium自动测试库，打开百度网，搜索苍老师，获取html等
Preparation:
网址：www.baidu.com
input-id：kw
button-id：su
"""
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

input = driver.find_element_by_css_selector('#kw')
input.send_keys("苍老师照片")

button = driver.find_element_by_css_selector('#su')
button.click()


a = driver.current_url
b = driver.get_cookies()
c = driver.page_source
d = input.text
print(a)
print(b)
print(c)
print(d)
