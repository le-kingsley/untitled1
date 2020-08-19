"""
贪心算法用python实现
场景：
假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。
很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。

名称	价格（美元）	重量（kg）
电脑	200	20
收音机	20	4
钟	175	10
花瓶	50	2
书	10	1
油画	90	9

输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""
class Thing(object):
    __slots__ = ('_name', '_dollar', '_weight')

    def __init__(self, name, dollar, weight):
        self._name = name
        self._dollar = dollar
        self._weight = weight

    @property
    def value(self):
        #价格重量比
        return self._dollar/ self._weight

def input_thing():
    #输入物品信息
    name_str, dollar_str, weight_str = input().split()
    return name_str, int(dollar_str), int(weight_str)

def main():


if __name__ == '__main__':
    main()