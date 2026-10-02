import os

"""文件/文件夹重命名"""
# os.rename(旧名字,新名字)
# os.rename("小吉祥草王.png",r"D:\code\图片\纳西妲.png")
# 同时rename还能移动文件,在同磁盘下移动效率非常高

"""删除文件/文件夹"""
# os.remove()test.txt
# os.rename("实验.txt")

"""创建文件夹"""
# os.mkdir()
# os.mkdir()

"""删除文件/文件夹"""
# os.rmdir()
# os.rmdir()

"""获取当前目录路径"""
# os.getcwd()
# print(os.getcwd())

"""获取目录列表"""
# 不写东西默认获取当前文件的目录列表
# print(os.listdir(r"D:\py临时项目"))
# print(os.listdir("../"))   # 获取上一级的文件夹目录列表


"""
迭代器:可以记住遍历位置的模块
可迭代对象:可以通过for...in...这类语句遍历读取数据的对象称之为可迭代对象
# 目前学过的可迭代对象:str/list/tuple/dict/set
遍历(迭代):依次从对象中把一个个元素取出的过程
可迭代对象的条件
1.对象实现了__iter__() 方法
2.__iter__() 方法返回了迭代器
"""
# for循环工作原理
# 1.先通过__iter__() 获取到可迭代对象的迭代器
# 2.对获取到的迭代器不断调用__next__()方法来获取下一个值并复制给临时变量
# isinstance(o,t)方法可以判断一个对象是否是可迭代对象,或者是一个已知的数据类型
# o  对象       t  数据类型
# st = '123'
# from collections.abc import Iterable
# Iterable是可迭代对象的数据类型
# print(isinstance(st,Iterable))  # 判断st是不是可迭代对象
# print(isinstance(st,int))  # 判断st是不是int数据类型
# print(isinstance(st,(int,str)))  # 判断st是不是int或str数据类型


li = [1,2,3,4,5]

i = iter(li)
# i = li.__iter__() 与 i = iter(li) 等价
print(i)
try:
    print(next(i))
    # print(i.__next__()) 与 print(next(i)) 等价
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    # 取完元素后再next()会引发StopIteration异常
    print(next(i))
except Exception as e:
    print(e)

"""可迭代对象iterable和迭代器iterator"""
# 作用于for循环的就是可迭代对象
# 作用于next()的都是迭代器
# 可迭代对象并不一定是迭代器对象
# 可迭代对象(Iterable) > 迭代器对象(Iteraror),迭代器对象是可迭代对象的子集
# 有__iter__()方法是可迭代对象
# 有__iter__()方法和__next__()方法是迭代器
'''
dir()  可以查看对象里的所有属性和方法
'''








