
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


# li = [1,2,3,4,5]

# i = iter(li)
# # i = li.__iter__() 与 i = iter(li) 等价
# print(i)
# try:
#     print(next(i))
#     # print(i.__next__()) 与 print(next(i)) 等价
#     print(next(i))
#     print(next(i))
#     print(next(i))
#     print(next(i))
#     # 取完元素后再next()会引发StopIteration异常
#     print(next(i))
# except Exception as e:
#     print(e)

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

"""自定义迭代器类"""
# 两个特性
# __iter__()和__next__()
# class Test(object):
#     """不同的类,不是迭代器类"""
#     def __init__(self):
#         self.num = 1
#     def funa(self):
#         print(self.num)
#         self.num += 1

# te = Test()
# print(dir(te))
# for i in te:
#     print(i)
'''报错:不是可迭代对象'''

"""自定义iter和next"""
# class MyIterator(object):
#     def __init__(self):
#         self.num = 0
#     def __iter__(self):
#         return self  # 返回的是当前迭代器类的实例对象
#     def __next__(self):
#         if self.num == 10:
#             raise StopIteration("终止迭代")
#         self.num += 1
#         return self.num

# mi = MyIterator()
# print(mi)
# for i in mi:    # for循环本质是调用对象的__next__()方法
#     print(i)


"""
生成器(genereator):一边循环一边计算的机制叫做生成器
列表数据过多时会占用大量的空间,生成器惰性求值,不耗内存
"""
# 生成器表达式
# li = [i*5 for i in range(5)] # 这是列表推导式
# gen = (i*5 for i in range(5)) # 这是生成器表达式
'''取出数据'''
# print(next(gen))
# print(next(gen))
# print(next(gen))

# 生成器函数
# python中使用了yield关键字就称之为生成器函数
# yield的作用:
# 1.类似return,将指定值或者多个值返回给调用者
# 2.yield语句一次返回一个结果,再每个结果中将,挂起函数,执行__next__(),再重新从挂起点继续往下执行
# 使函数中断,并保存中断的状态
# def test():
#     """普通函数"""
#     li = []
#     li.append("a")
#     li.append("b")
#     print(li)

# test()
'''局部变量从头开始'''
# test()


# def gen():
#     """使用了yield语句-->生成器函数"""
#     yield 'a'  # 返回一个'a',并暂停函数,在此处挂起,下一次再从此处回复执行
#     yield 'b'
#     yield 'b'

# gen_1 = gen()
# print(gen_1)  # 迭代器
# print(next(gen_1))    # 从迭代器函数去取值
# print(next(gen_1()))  # 调用函数,每次都是a

# 可迭代对象 > 迭代器 > 生成器
"""
总结:
1.迭代器对象:实现python迭代协议,可被for...in...遍历取值
2.迭代器:可以记住自己遍历位置的对象,直观体现:可以使用next()函数返回值,迭代器只能往前,不能往后
3.生成器:本质就是迭代器,是特殊的迭代器,它是Python提供的通过简单的方法写出迭代器的一种手段
"""
