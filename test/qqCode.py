"""
正则表达式：查找符合复杂关系的字符串时，描述规则时使用的工具，定义字符串匹配模式

"""

import re

def main():
    username = input('请输入用户名：')
    qq = input('请输入qq号：')
    # 用户名信息在数字、大小写字母、下划线中取6-20次
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('请输入有效的用户名！')
    # 用户在1-9中取值，取数字4-11次
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的qq号！')
    if m1 and m2:
        print('有效信息！')

if __name__ == '__main__':
    main()