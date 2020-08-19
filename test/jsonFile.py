"""
JSON file
json文件的读写，方便各个程序间的数据交互
dump:将python对象按JSON格式序列化到文件中
dumps:将python对象处理成JSON格式的字符串
load:将文件中的JSON数据反序列化成python对象
loads:将字符串内容反序列化成python对象
"""

import json

def main():
    mydict= {
        "name": "张三",
        "age": "38",
        "e-mail": "15603250635",
        "friends": ["李四", "王五"],
        "cards": [
            {"brand": "奔驰", "value": 500000},
            {"brand": "宝马", "value": 300000},
            {"brand": "大众", "value": 100000}
        ]
    }
    try:
        with open('D:\\data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存文件成功！')

if __name__ == '__main__':
    main()