'''
# helloWorld.py
# Copyright (C) 2019 ...
# Author : Huangtao
# Version: V1.0.0  2019-09-22 Create
# Description:
#
'''
import keyword # python 关键字
#print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
# 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
# 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
# 'try', 'while', 'with', 'yield']

print("Hello World!")
message = "Author: Huangtao" # 注意：单引号，双引号，三引号的区别
print(message)
print(message.upper())
year = 2019 # int, float, bool, complex
temp = 26.5
ok = True
x = 3+4j
print("Today: " + str(year) + ", Temp: " + str(temp) + ", " + str(ok))
print(str(type(x)) + ", " + str(isinstance(x, complex)))

# Python3 6个标准数据类型
# 不可变数据：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据  ：List（列表）、Dictionary（字典）、Set（集合）
# Example:
list1 = [2018, 2019, 'low', 'high', 26.1, 26.2]
print(list1[-3:-1] * 2, list1.index(2018)) # ['high', 26.1, 'high', 26.1] 0
tuple1 = (1, 'one')
print(tuple1 + tuple((2, 'two')))
dict1 = {'Name':'Tao', 'Age':20} # 键必须不可变，数字、字符串、元组
print("dict['Age']: ", dict1['Age'])
set1 = set('aabbccdd') # 集合是一个无序的不重复元素序列
set1.add("BBC")
print(set1)



