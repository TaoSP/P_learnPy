"""
# classTest.py
# Copyright (C) 2019 ...
# Author : Huangtao
# Version: V1.0.0  2019-09-25 Create
# Description: Class,
#
"""

# 类方法必须包含参数self，且为第一个参数，self代表的是类的实例
# self名字并不规定，也可用this或其它
class Car:
    name = 'H'
    __cost = 10000 # 私有属性
    def __func1(self): # 私有方法
        return
    def __init__(self, n): # 构造函数
        self.name = n
    def __del__(self): # 析构函数
        print("bye")
    def info(self):
        print("Hi car: %s" %(self.name))
        return
x = Car('Tao')
x.info()
del x

class NewCar(Car): # 单继承
    weight = 2000
    def __init__(self):
        Car.__init__(Car, 'Tao1')
        Car.info(Car)
    def info(self): # 方法重写
        print("NewCar")
x1 = NewCar()
x1.info()
super(NewCar, x1).info() # 调用父类被覆盖的方法

# 类的专有方法
# __init__, __del__, __str__, __cmp__, __add__, ...

# 运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)
    def __str__(self):
        return 'Vector: a = %d, b = %d' %(self.a, self.b)
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)

