
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



"""

多任务

"""
# 导入时间模块
import time

# def A():
#     print("执行A函数")
#     '''time.sleep(int) 等待int时间后再执行下面的代码'''
#     time.sleep(2)  # 以秒为单位
#     print("2秒过后")

# def B():
#     print("执行B函数")


'''
多线程
1.线程：资源cpu调度的基本单位,每一个进程至少都会有一个线程,这个线程通常就是我们所说的主线程
2.进程：是资源赵作系统进行资源分配的基本单位，每打开一个程序至少就会有一个进程
一个进程默认有一个线程，进程里面可以创建多个线程，线程是可以依附在进程里面的，没有进程就没有线程
'''

# 导入线程模块
import threading
# Thread线程参数
# target:执行的任务名
# args:以元组的形式给任务传参
# kwargs:以字典的形式传参
"""
def A():
    print("执行A函数")
    time.sleep(2)
    print("A函数已执行完毕")

def B():
    print("执行B函数")
    time.sleep(2)
    print("B函数已执行完毕")

# 主程序入口
if __name__ == "__main__":
    # 1.创建子线程
    t1 = threading.Thread(target=A) # 函数不加小括号
    # print(t1)
    t2 = threading.Thread(target=B)
    # 3.守护线程,必须放在start()前面:主线程结束,子线程也会跟进来
    # 作用:在后台运行,当主线程执行完毕,且没有存活的非守护线程时,整个python程序会直接退出,守护线程也被强制终止
    t1.daemon = True
    t2.daemon = True
    # 2.开启子线程
    '''使用start()方法'''
    t1.start()
    t2.start()
    # 4.阻塞主线程join():暂停的作用,等子线程执行结束后,主线程才会继续执行,必须放在start()后面
    t1.join()
    t2.join()
    # 获取线程名字
    print(t1.name)
    print(t2.name)
    # 更改线程名字
    t1.name = "线程-1"
    t2.name = "线程-2"
    print("运行结束")

"""
'''
线程特点:
1.线程之间共享资源
'''
# 1
# li = [] # 全局变量
# # 写入数据
# def wdata():
#     for i in range(5):
#         li.append(i)
#         time.sleep(0.2) # 循环5次就是1秒
#     print("写入数据:",li)
# # 读取数据
# def rdata():
#     print("读取的数据是",li)
# if __name__ == "__main__":
#     # 创建子线程
#     t1 = threading.Thread(target=wdata)
#     t2 = threading.Thread(target=rdata)
#     # 开启子线程
#     t1.start()
#     # 阻塞线程
#     t1.join() # 加了join()就会等待t1任务执行结束
#     # time.sleep(1) 不阻塞线程,等待的时间要和上面的216行匹配
#     t2.start()
#     t2.join
'''
2.资源竞争
'''
# a = 0 # 全局变量
# b = 1000000 # 循环次数
# def add():
#     global a
#     for i in range(b):
#         a += 1
#     print("add:",a)

# def add2():
#     global a
#     for i in range(b):
#         a += 1
#     print("add2:",a)
# # add() # 1000000
# # add2() # 2000000

# if __name__ == "__main__":
#     f1 = threading.Thread(target=add)
#     f2 = threading.Thread(target=add2)
#     f1.start() # 完全随机,两个线程竞争同一个局部变量
#     f2.start()

'''
3.线程同步
'''
# 1.join线程阻塞

# a = 0
# b = 1000000
# def add():
#     global a
#     for i in range(b):
#         a += 1
#     print("add:",a)

# def add2():
#     global a
#     for i in range(b):
#         a += 1
#     print("add2:",a)

# if __name__ == "__main__":
#     f1 = threading.Thread(target=add)
#     f2 = threading.Thread(target=add2)
#     f1.start()
#     f1.join() # 等待第一个子线程执行完后再执行下一个子线程
#     f2.start()

# 2互斥锁:对共享数据进行锁定,保证多个线程访问共享数据不会出现数据错误问题:保证同一时刻只能有一个线程去操作
# acquire():上锁
# release():释放锁
# 这两个方法必须成对出现

from threading import Thread,Lock # 导入模块

# 2创建互斥锁
# lock = Lock()

# a = 0
# b = 1000000
# def add():
#     lock.acquire() # 上锁
#     global a
#     for i in range(b):
#         a += 1
#     print("add:",a)
#     lock.release() # 解锁

# def add2():
#     lock.acquire() # 上锁
#     global a
#     for i in range(b):
#         a += 1
#     print("add2:",a)
#     lock.release() # 解锁


# if __name__ == "__main__":
#     f1 = threading.Thread(target=add)
#     f2 = threading.Thread(target=add2)
#     f1.start()
#     # f1.join()
#     f2.start()

# 互斥锁是多个线程一起争夺,抢到锁先执行



"""
进程:是操作系统进行资源分配和调度的基本单位,是操作系统结构的基础
一个正在进程的程序或软件就是一个进程
进程里面可以创建多个线程,一个进程至少有一个线程
"""

'''
1.进程的状态
就绪状态:运行的条件满足,正在等待CPU执行
执行状态:CPU正在执行其功能
等待(阻塞)状态:等待某些条件满足(程序未响应等等)
'''

'''
进程语法结构
'''
from multiprocessing import Process # 提供了Process类代表进程对象

# Process 类参数
# 1.target:执行的目标任务名,即子进程要执行的对象
# 2.args:以元组的形式传参
# 3.kwargs:以字典的形式传参
# 4.name:给子进程设置名字

# Process 方法
# 1.start():开启子进程
# 2.is_alive():判断子进程是否还活着,存活返回Turn,否则返回Flash
# 3.join():主进程等待子进程执行结束

# Process 属性
# name:当前进程的别名,默认为Process-N
# pid:当前进程的进程编号

def A():
    print(111)
def B():
    print(222)
    
if __name__ == "__main__":
    # 创建子进程
    p1 = Process(target=A,name="a") # 可以给子进程命名
    p2 = Process(target=B)
    # 开始子进程
    p1.start()
    p2.start()
    print("p1:",p1.name)
    print("p1:",p2.name)
    
    
    
    
    
    
    