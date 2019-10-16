'''
# algorithmSort.py
# Copyright (C) 2019 ...
# Author : Huangtao
# Version: V1.0.0  2019-10-06 Create
# Description: algorithm, sort, 
#
'''

'''
# Input Output Test: A+B
t= int(input())
while (t>0):
    a = []
    for x in input().split():
        a.append(int(x))
    print(sum(a))
    t -= 1
'''

def getInputList():
    a = []
    #  Python3 raw_input和input进行了整合, 仅保留input
    for x in input("Please input: ").split():
        a.append(x)
    return a

def bubbleSort(list1):
    size = len(list1)
    for i in range(size):
        # 从大到小
        #for j in range(i):
        #    if(list1[i] > list1[j]):
        #        # Python多重赋值，右边从左到右先完成计算
        #        list1[i], list1[j] = list1[j], list1[i]
        # 从小到大
        for j in range(i, size):
            if(list1[i] > list1[j]):
                list1[i], list1[j] = list1[j], list1[i]
    return list1

if __name__ == '__main__':
    print(__name__)
    list1 = bubbleSort([9,1,2,5,3,8,6])
    print(list1)





