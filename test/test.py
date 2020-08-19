"""
Title:numpy leaning
Author:kingsley
Version:0.1
Question:机器学习入门
KNN流程：
1.收集数据
2.数据结构化
3.分析数据
4.训练算法
5.测试算法
6.使用算法
"""
from numpy import *

if __name__ == '__main__':
    randMat = mat(random.rand(4, 4))
    rerandMat = randMat.I
    print(randMat)
    print(rerandMat)
    myEye = randMat*rerandMat-eye(4)
    print(myEye)
    print(set)