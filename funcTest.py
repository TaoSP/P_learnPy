'''
# funcTest.py
# Copyright (C) 2019 ...
# Author : Huangtao
# Version: V1.0.0  2019-09-23 Create
# Description: if, while, for, def, try,
#
'''

a, b = 1, 3
print(a, end=', ')
print(b)

year = 2018
if year == 2018:
    print(2018)
elif year == 2019:
    print(2019)
else:
    pass # 空语句

count = 3
while count > 0:
    print(count, end=', ')
    count -= 1
else: # else语句在while循环条件变为false 或 在for循环穷尽列表终止时被执行，但break终止时不执行
    print()

num = [1, 2, 3, 4]
for x in num: # break, continue
    print(x, end=', ')
else:
    print()

it = iter(num) # 创建迭代器对象
for x in it:
    print(x, end=' ')
print("iter1 ok")

def funcNum(n):
    a = 0
    while True:
        n -= 1
        if (n < 0):
            return
        yield a # yield 生成器
        a += 3
it2 = funcNum(5) # 迭代器2，由生成器返回生成
while True:
    try:
        print(next(it2), end=' ')
    except StopIteration: # try 语句可包含多个except子句
        break
    #except:
    #    raise
    #else: # 没有发生任何异常时执行
    #    break
    #finally: # 任何情况下都会执行的清理行为
    #    print("try done")
print("iter2 ok")

# 函数的参数传递：
# 不可变类型、可变类型
# 关键字参数，默认参数
def func2(arg1, *vartuple, year, age = 18): # 加 *参数会以tuple导入，**参数会以字典形式导入
    print(arg1, vartuple, year, age, end=' ')
    print("fun2 ok")
    return
func2(20, 30, 40, year=2019) # 出现 *后的参数必须用关键字传入

# 列表推导式
list1 = [1, 2, 3, 4, 5]
list2 = [2*x for x in list1 if (x > 2)]
print(list2)
list3 = [2, 3]
list4 = [x*y for x in list1 for y in list3] # 循环技巧
print(list4) # [2, 3, 4, 6, 6, 9, 8, 12, 10, 15]

# File, OS
import os
print(os.getcwd())
file1 = os.getcwd() + "\\funcTest.py"
print(file1)
print(os.path.isfile(file1))


