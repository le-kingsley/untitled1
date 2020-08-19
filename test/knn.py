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
import operator


def createDateSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dateset, labels, k):
    datasetsize = dateset.shape[0]
    # 计算距离
    diffMat = tile(inX, (datasetsize, 1)) - dateset
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)

    distances = sqDistances**0.5
    sortedDistances = distances.argsort()
    classCount = {}
    # 选择距离最小的k个点
    for i in range(k):
        voteIlabel = labels[sortedDistances[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # 排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


if __name__ == '__main__':
    group, labels = createDateSet()
    print(classify0([1, 1], group, labels, 3))

