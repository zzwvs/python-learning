"""
格式化输出
%s 字符串
%d 整数
%f 浮点数

f格式化
print(f"{变量名}")
"""

"""
+加
-减
*乘
/除
//取整数
%取余数
**幂
"""

"""
input输出函数
if判断
"""
"""
输出输入函数,if判断
"""
# a = input("请输入姓名：")
# print(f"你的姓名是:{a}")
# print(type(a))
# a = input("请输入密码：")
# b = "123"
# if a == b:
#     print("密码正确")
# else:
#     print("密码错误")

"""
==等于
!=不等于
and左右两边都符合才True
or符合一个就为True
not相反的结果
"""


"""
if判断扩展
"""
# c = input("请输入：")
# if c == "999":
#     print("真棒")
# else:
#     print("继续加油")


# if elif
# if 条件1:
#     满足条件1运行
# elif:条件2
#     满足条件2运行
#     ......

"""
if嵌套(注意缩进)
if 条件1:
    命令1
    if 条件2:
        命令2
    ......
else:
    命令3
"""


"""
创建列表,索引,修改列表里元素,一些内置函数,删除元素
"""
# lend = ['哈哈','嘻嘻','呵呵','cannondale','redline']
# print(lend[-1].title())    #title()输出首字母大写
# print(lend)

# liebiao1 = '我喜欢' + lend[0] + '大笑'  #用lend的值生成句子
# print(liebiao1)

# lend[0] = '啦啦'    #修改列表里的元素
# print(lend)

# lend.append('honda')    #append()将元素添加到末尾
# print(lend)

# lend.insert(1,'啦啦')   #insert()在列表人员位置插入元素
# print(lend)

# del lend[2] #del语句删除列表中的元素
# print(lend)



# acft = ['a','b','c','d','e']
# ance = acft.pop(-1)     #使用pop()可弹出列表中的元素并储存到变量中，可返回值不像del语句只是删除元素
# print(acft)
# print(ance)

# acft_1 = 'b'
# acft.remove(acft_1)        #remove()根据值删除元素,也可以继续使用它的值存储在变量中
# print(acft)


"""
遍历列表,一些函数
"""
# names = ['zzw','wxf','klee','xh','gybz','7430']

# for name in names:      #将names中的每一个值存储到name中
#     #for循环可以将代码重复执行，直至列表后面没有元素才停止
#     print(name + ' hello')
# #每个缩进的代码都是循环的一部分
# print('很高兴见到你们')     #没有缩进的代码只会执行一次

# for shuzhi in range(1,5,):   #函数range(a,b,c)可以存储从a到b-1的整数,步长c只能是整数
#     print(shuzhi)

# mas = list(input(("请输入列表:")))      #函数list()可以将元素转换成列表
# print(mas)

# for i in range(0,10):   #可以用这种方法生成小数,生成0.0,0.1,0.2,......0.9
#     s = i / 10.0      # 使用分数可以避免浮点数误差
#     print(s)

# pinfan = []     #创建一个包含前10个整数的平方的列表
# for i in range(1,10):
#     pinfan.append(i**2)
# print(pinfan)

# pinfan = [i**2 for i in range(1,10)]    #列表解析
# print(pinfan)


"""
一些内置函数,切片,创建副本
"""
#     #代码5
# d = [1,5,0,6,0,7,8,2,2,5,4,7,6]
# print(min(d))   #最小值
# print(max(d))   #最大值
# print(sum(d))   #求和

# j = []      #生成0到99的奇数
# for i in range(1,100,2):
#     j.append(i)
# print(j)

# l = []      #生成0到99能被3整除数
# for i in range(1,100):
#     if i % 3 == 0:
#         l.append(i)
# print(l)

# print(j[0:3])   #使用冒号':'进行切片
# print(j[-3:])   #没加索引默认为开头/末尾


# my_food = ['pizza','falafel','carrot','cake']
# you_food = my_food      #赋值,名字不同但指向同一个列表
# you_food = my_food[:]   #创建列表副本,两个不同的列表


"""
创建元组,修改元组的方法,与列表的区别
"""
# cs_tuple = (1,2,3,4,5,6,7,8,9)    #定义一个元组,它是一个不可被改变的列表
# # cs[0] = 2       #元组不能被改变,此时报错

# #修改元组的方法
# #1.重新赋值
# cs_tuple = (1,3,5,7,9)
# print(cs_tuple)
# #2.转换成列表修改,再转换成元组
# cs_list = list(cs_tuple)
#           行为    遍历范围        帅选条件
# cs_list = [x for x in cs_list if x %2 != 0]     #列表推导式
# print(tuple(cs_list))


"""
创建字典,添加键值对,修改字典的值,删除字典的元素
"""
# alien_0 = {'color':'green','points':5}      #定义一个字典,一个键对应一个值
# print(alien_0['color'])     #访问字典中的值
# print(alien_0['points'])
# print(alien_0)
# alien_0['x_position'] = 0       #在字典添加键-值对
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0['color'] = 'yellow'     #修改字典的值,与列表类似

# del alien_0['points']       #删除字典的元素
# print(alien_0)


"""
遍历字典的键值对，遍历字典的键,遍历字典的值,函数sorted()可对其排序
"""
# my_dict = {'a':1,'b':2,'c':3}
# for key,value in my_dict.items():       #使用方法.items()遍历字典的键值对
#     print(f'key:{key},value:{value}')       #key是键,value是值
    
# for i in my_dict.keys():        #使用方法.keys()遍历字典的键
#     print(i)
# for x in sorted(my_dict.keys()):    #函数sorted()可对其排序,下同
#     print(x)

# for i in my_dict.values():      #使用方法.values()遍历字典的值
#     print(i)
# for x in sorted(my_dict.values()):
#     print(x)


"""
将字典重复的键/值去除
"""
# m = {'a':1,'b':2,'c':3,'d':2,'e':3}
# for i in sorted(set(m.values())):       #函数set()可利用集合的特性将字典重复的键/值去除,sorted()进行排序(可以不写)
#     print(i)        #打印不重复的值,不能修改字典

# seen_values = set()
# new_m = {}
# for key,value in m.items():
#     if value not in seen_values:        #如果值没出现,就加入新字典
#         new_m[key] = value
#         seen_values.add(value)      #.add()是集合的内置方法,用于在集合中添加元素
# print(new_m)        #修改字典本身


"""
while循环,标志变量,continue语句可回到循环开头,break语句可结束循环
"""
# num = 1
# bz = True
# while bz:
#     if num <= 5:
#         print(num)
#         num = num + 1
#     else:
#         a = input('是否继续/停止:')
#         if a == '继续':
#             num = 1
#         elif a == '停止':
#             print('程序已停止')
#             bz = False

# number = 0
# while number < 10:
#     number += 1
#     if number % 2 == 0:
#         continue        #continue语句可回到循环开头,break语句可结束循环
#     print(number)
        

"""
......
"""
# 在列表之间修改元素
# names = ['alice','brian','candace','zzw','klee']
# new_name = []
"""意义不明
while True:
    if names != []:
        mun = names.pop(0)       #.pop(0)可以保持原始排序
        new_name.append(mun)
    else:
        print((new_name))
        break
"""
# new_name = names[:]     #更简洁
# print(f'{names}\n{new_name}')


"""
删除包含特定值的元素,方法remove()可删除列表中的特定值,如果特定值出现不止一次就要结合while
"""
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)
# pets_set = set(pets)
# print(list(pets_set))


"""
使用用户输入来填充字典
"""
# b = []
# while True:
#     a = input('输入:')
#     if a != '输出':
#         b.append(a)
#     else:
#         print(b)
#         break

# responses = {}
# is_running = True
# while is_running:
#     i = input('是否愿意参加此次调查:').strip()      #方法.strip()可去掉首尾空格
#     if i == '是':
#         k = input('请输入你的名字:')
#         v = input('请输入你的回答:')
#         responses[k] = v
#         print('记录成功')
#     elif i == '否':
#         print(f'感谢您完成调查,以下是调查结果: \n{responses}')
#         is_running = False
#     else:
#         print('输入无效,请重新输入"是"或"否"')
#         continue


"""
定义函数
"""
# def greet_user():       #定义一个简单的函数
#     print("hello")
# greet_user()

# def hello_user(username):       #可在括号内指定一个值
#     print('hello,' + username.title() + '!')
# hello_user('Jesse')     #调用函数时可传递给它
"""
def greet_user(形参):
    ......
greet_user(实参)
"""
#传递实参
# #1.位置实参
# def describe_pet(animal_type,pet_name):
#     print("\nI have a" + animal_type + ".")
#     print('My' + animal_type + "'s name is " + pet_name.title() + '.')
# describe_pet('hamster','harry')
# #2.关键字实参
# def describe_pet(animal_type,pet_name):
#     print("\nI have a" + animal_type + ".")
#     print('My' + animal_type + "'s name is " + pet_name.title() + '.')
# describe_pet(animal_type='hamster',pet_name='harry')
# # 3.默认值实参
# def describe_pet(pet_name,animal_type='dog'):       #有等号的(默认参数)放在右边,因为本质还是位置实参
#     print("\nI have a" + pet_name + ".")
#     print('My' + animal_type + "'s name is " + animal_type.title() + '.')
# describe_pet('harry')
#返回值:return会给函数返回值
# def 买():
#     return'一桶水果茶',20       #return返回多个值以元组的形式,没有返回值就返回None
#     print('一桶水果茶')     #遇到return函数结束下面的代码不会被执行
# 买
# print(买())

# muns = [1,2,3,4,5,6,7,8,9]
# def fxg(mun):
#     mun_jishu = []
#     mun_oushu = []
#     for i in mun:
#         if i % 2 != 0:
#             mun_jishu.append(i)
#         else:
#             mun_oushu.append(i)
#     print(mun_jishu)
#     print(mun_oushu)

# fxg(muns[:])      #防止函数修改列表
# print(muns)


"""
全局变量和局部变量
"""
# a = '哈哈'      #函数体外的变量是全局变量
# def 全局和局部变量():
#     global b    #关键字global可以将后面的变量声明为全局变量
#     b = '嘻嘻'
#     c = '呵呵'    #函数体内的变量是局部变量,只能在函数内被调用
# 全局和局部变量()    #调用函数后才能使用函数里的全局变量,如果没有这一行代码print(b)将报错
# print(a)
# print(b)
# print(c)        #c未被定义,报错


"""
nonlocal的用法
"""
# a = 10                  #全局变量
# def outer():            #外函数
#     a = 5               #局部变量
#     def inner():        #内函数
#         nonlocal a      #这行命令告诉python,不要创建新变量,而是去上一层中找a
#         a = 10
#         print('inner函数中a的值:',a)
#         def inner2():
#             nonlocal a
#             a = 20
#             print('inner2函数中a的值:',a)
#         inner2()
#     inner()
#     print('outer函数中a的值:',a)
    
# outer()
##嵌套传递：nonlocal 是向上一层找变量，如果上一层也是 nonlocal 绑定的，
##它就会沿着作用域链顺藤摸瓜，找到最原始的那个外层变量


"""
匿名函数
"""
#函数名 = lambda 形参:返回值(表达式)
#普通函数
# def add(a,b):
#     return a + b
# print(add(1,3))
# #匿名函数
# add = lambda a,b:a + b
# #lambda不需要写return来返回值，表达式本身就是返回值
# print(add(1,3))
# #无参数
# funa = lambda:'hello'
# print(funa())
# #一个参数
# funb = lambda name:name
# print(funb('zzw'))
# #默认参数
# func = lambda name,age=18:(name,age)        #返回值以元组的形式输出!
# print(func('zzw',12))


"""
三目运算
"""
##为真结果 if 条件 else 为假结果     (三目运算，也用于列表推导式或数字生成器)
# comp = lambda a,b:'a比b小' if a < b else 'a大于等于b'
# print(comp(5,8))
#lambda只能实现简单逻辑


"""
部分常用内置函数
"""
#查看所有的内置函数
#import builtins
#print(dir(builtins))    #大写开头一般是内置常量名，小写字母开头一般是内置函数名

#   内置函数一
#abs() 返回绝对值,里面只能有一个数字
#print(abs(-5))

#sum() 求和∑
#print(sum([1,2,3,4,5,6]))    #sum求和必须是可迭代对象:列表、集合、元组，没有字典、字符串、整形、浮点型

#min()最小值    max()最大值
#print(min(-8,6,key=abs))    #传入了求绝对值函数，则参数就会先求绝对值再比较大值

#zip():将可迭代对象作为参数，将对象中对应的元素打包成一个个元组
# li = [1,2,3]
# li2 = ['a','b','c']
# print(zip(li,li2))
# # 取出元素   1.for循环
# for i in zip(li,li2):
#     print(i)
# li2 = ['a','b']
# for i in zip(li,li2):
#     print(i)
# #2.转换成列表打印
# print(list(zip(li,li2)))

#map():可以对可迭代对象的每一个元素进行映射，分别去执行
#map(自己定义的函数,放进去的可迭代对象)     简单说就是对象中的每一个元素都会去执行这个函数
# li = [1,2,3]
# def funa(x):
#     return x*5
# mp = map(funa,li)
# print(mp)       # 打印出的是内存地址
# for i in mp:
#     print(i)
# print(list(mp))         #map返回的是一个迭代器,迭代器是一次性的,用完就没

#reduce():对参数中的元素进行累积,需要先导包
# from functools import reduce
# #reduce(函数,可迭代对象)
# li2 = [1,2,3,4]
# def add(x,y):
#     return x+y
# res = reduce(add,li2)
# print(res)


"""
拆包:对于函数中的多个返回数据，去掉元组，列表，或者字典 直接获取里面的数据的过程
"""
# tua = (1,2,3,4)
# print(tua)
# #方法一
# a,b,c,d = tua
# print(a,b,c,d)  #要求元组内的个数与接收变量的个数相同

# #方法二
# a,*b = tua
# print(a,b)
# c,d,e = b
# print(c,d,e)


"""
自定义一个异常
"""
# raise Exception('异常')
# def funa():
#     print('哈哈哈')
#     raise Exception('异常')     #raise语句后面的代码不会被执行
#     print('嘻嘻嘻')
# funa()

# def mima():
#     q = input('输入不小于6位数密码:')
#     if len(q) >= 6:
#         return '输入成功'
#     else:
#         print('输入失败')
#         raise Exception('密码长度不足')
# # print(mima())

# try:    #尝试执行包裹可能引发错误的代码块,如果执行顺利就跳过except块,继续执行后面的代码
#     print(mima())
# except Exception as e:  #将错误信息存储在e中,except语句紧跟在try后面,用于捕获并处理try块中发生的错误
#     print(e)


"""
模块
"""
#模块:一块py文件就是一个模块,导入一个模块就是执行一个py文件
#分类:
#1.内置模块
#random,time,os,logging......
#直接导入即可使用
#2.第三方模块(第三方库)
#3.自定义模块
#导入模块
# import ku       #导入整个模块
# print(ku.模块1())   #必须加括号才算调用

# from ku import 模块1,模块2      #导入模块中特定的函数
# print(模块1())      #必须加括号才算调用

# from ku import *        #模块里的所有内容全部导入,包括函数/变量,可能会有冲突


# import ku as pt         #as给模块起别名
# print(pt.模块1())

# from ku import 模块1 as pt,模块2 as ad
# print(pt())
# print(ad())

"""
包
"""
#含义：项目结构中的文件夹/目录
#区别：包有__init__.py的文件夹

# from pack import pa01       #使用这种方法会执行__init__和pa01
# pa01.mun()

# import pack                 #使用这种方法只会执行__init__

# import my_package

# __all__:本质上是一个列表
# 可以控制要引入的东西
# from my_package import *
# py01.HW()
# import *的行为:1.没有__all__ 导入模块中所有不以下划线_开头的名字
                #2.有__all__ 只导入列表中列出的名字,其余全部忽略
# from pack import *
# pa01.mun()


"""
递归函数
条件:1.必须有一个明确的条件---递归出口 2.没进行更深层次的递归,问题规模相比上次递归都要有所减少 
3.相邻两次重复之间有紧密联系
"""
# def add():      #普通函数
#     s = 0
#     for i in range(1,101):
#         s = s + i
#     print(s)
# add()
'''
def add1(n):
    return sum(range(1,n+1))
print(add1(3))
'''

'''
def add2(n):        #递归函数
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + add2(n-1)        # 3 + add(2)--->3 + 2 + add(1)--->3 + 2 + 1 + add(0),
    # 但add(0)只是虚构不可能执行--->3+2+1=6
print(add2(3))
'''

'''
from functools import reduce        #回顾之前reduce的内容
def add3(n):
    def add_3(x,y):
        return x+y
    return reduce(add_3,range(1,n+1))
print(add3(3))
'''

'''
def 斐波那契数列(n):        # 1.1.2.3.5.8.13.21.34......
    if n <= 1:
        return n
    else:
        return 斐波那契数列(n-1) + 斐波那契数列(n-2)

for i in range(1,10):
    print(斐波那契数列(i))

print(list(map(斐波那契数列,range(1,10))))
'''


"""
闭包
条件 1.嵌套函数
    2.内层函数使用外层函数的局部变量
    3.外层函数的返回值是内层函数的函数名
"""
# def outer():
#     m = 10
#     def inner():
#         print(m)
#     return inner    # 返回内函数的内存地址

# print(outer())      # 返回的是内部函数的内存地址
# 第一种写法
# outer()()       # outer()返回内部函数的内存地址,后面紧接着()执行了inner()
# 第二种写法
# ot = outer()    # 只执行outer(),得到函数对象并赋值给ot就变成了闭包函数
# ot()            # 直接调用ot相当于调用了之前的inner()

# print(ot())     # 打印一个函数如果没有返回值就默认返回None

# def fun1(m):
#     n = 10
#     def fun2():
#         return f'计算结果,{n + m}'
#     return fun2

# print(fun1(20)())       # 函数字有在被调用时才会被执行


# def o(m):
#     print('o中函数的值',m)
#     def i(n):
#         print('i中函数的值',n)
#         return m + n
#     return i

# ot = o(5)       # 给外函数传值
# print(ot(10))   # 给内函数传值
"""
函数id()可以查看内存地址
"""
# a = 1
# print(id(a))    # 打印a的内部储存地址
# b = a
# print(id(b))    # a和b是同一个地址


"""
装饰器:本质上就是一个闭包函数
作用:在不改变原有代码的情况下添加新的功能
条件:1.不修改源程序或代码
     2.不改变函数或程序的调用方法
"""

# def test02():
#     print('登录成功')

# def test(t2):
#     print('开始注册')
#     print('正在登陆')
#     t2()        # 调用要传入的函数

# test(test02)


# def test03():
#     print('开始注册')
#     print('正在登陆')
#     test02()

# test03()

# def fan1():
#     a = 10
#     def fan2():
#         nonlocal a
#         a = 20
#         def fan3():
#             nonlocal a
#             a = 30
#             return f'fan3-->,{a}'
#         print('fan2-->',a)
#         return fan3
#     print('fan1-->',a)
#     return fan2

# print(fan1()()())       # 10.20.30


"""
语法糖
@装饰器名称
"""
# def outer(fn):
#     def inner():
#         print('登录...')
#         return fn()
#     return inner

# @outer      # 以语法糖的形式调用send(),等价于 send = outer(send)
# def send():
#     print('发送消息:哈哈哈')
# # send = outer(send)      # @outer执行的等价代码
# send()


# def outer(fn):
#     def inner():
#         print('登录...')
#         return fn()     # 必须写return fn(),不要写fn()
        # print()打印返回值,rentun fn()就是返回send()的返回值,没有rentun就无法输出'发送消息:哈哈哈'
    # return inner

# def send():
#     return '发送消息:哈哈哈'

# print(outer(send)())


# def a(a_):
#     def b(b_):
#         return a_(b_)
#     print('这是被装饰的函数')
#     return b

# @a      # c = a(c)
# def c(b_):
#     print(f'这是b中的参数{b_}')
# # a(c)(111)
# c(111)


# def fan1(fn):
#     def fan2():
#         return fn()
#     return fan2

# @fan1
# def fan3():
#     print('返回值')
# fan3()
'''
可变参数:*args,**kwargs
'''
# def fana_1(c,*args,**kwargs):       # *args会把多余的位置参数打包成一个元组
#     # **kwargs会把多余的关键字参数打包成一个字典
#     print(args,kwargs,c)
    
# fana_1(666,'哈哈',b='呵呵')


# def fan_1(b):
#     def fan_2(*a):
#         return b(a)
#     return fan_2

# @fan_1      # fan_3 = fan_1(fan_3)
# def fan_3(c):
#     print(f'这是fan_2中的参数:{c}')

# fan_3(666,777)      # fan_1(fan_3)(666)


"""
面向过程:就是先分析出解决问题的步骤,再把步骤拆成一个个方法,
是没有对象去调用的,通过一个个方法的执行解决问题。

面向对象:就是将编程当成是一个事物(对象),对外界来说,事物是直
接使用的,不用去管内部的情况,而编程就是设置事物能做什么事
情。

类:对一系列具有相同属性和行为的事物的统称,是一个抽象的概
念,不是真实存在的事物。
基本格式:
class 类名:
    代码块
"""
# class Fan:          # 创建一个类
            # **后面不加括号,就是父类**
#     fan_1 = 123     # 类属性
#     fan_2 = 456
#     def fan1(self):
#         print('这是一个类方法')
#         return f'方法中的self:{self}'

# f1 = Fan()          # 创建对象(实例对象)
        # **后面要加括号**
# print(f1.fan1())
# self代表实例本身,带对象调用实例方法时,python会自动将对象本身的内存地址作为参数,传递到实例方法的第一个参数self里面


# class zzw_set:
#     name = 'zzw'
#     age = 18
#     hin = 171
#     like = ['玩','吃','睡','喝']
#     def zzw_1(self):
#         print(f'我叫{zzw_set.name}')
#         print(f'年龄是{self.age}')
#         for i in self.like:
#             print(f'平时喜欢{i}')
            
# zw = zzw_set()

# print(zw.loov)



# class Con:
#     动物 = 'dog'
#     年龄 = 8                # 类属性,所有实例共有
#     颜色 = 'yellow'
#     def __init__(self,m,kg):     # __init__是构造函数,导入类时都会执行,可以初始化实例属性
#         self.m = m     # 实例属性,实例特有
#         self.kg = kg

# p = Con('136',10)

# print(Con.动物)     # 类属性是共用的
# print(p.m)
# print(p.kg)
# print(p)        # 他们输出的内存地址都不一样
# print('==========')     # 不同的实例属性只在不同的实例方法中调用
# l = Con('100',12)
# print(p.年龄)
# print(l.m)
# print(l.kg)
# print(l)        # 他们输出的内存地址都不一样

# l.mmm = 666     # 实例属性也可以在外面定义
# print(l.mmm)

"""
设计class类是干嘛的,为什么不从其他文件中导入相应的功能呢?
首先，“设计类”和“从其他文件导入”是完全不矛盾的。实际上，你定义的类通常就是写在某个.py文件里,
然后通过,from module import MyClass,导入到其他文件中使用的。
模块化（文件级别）：解决的是“代码放在哪里”的问题，避免所有代码堆在一个文件里。
类（代码组织级别）：解决的是“数据和操作如何绑定”的问题。

函数式写法-->状态难管理
    全局变量容易被意外修改
类写法-->状态封装
    状态跟着实例走

类把相关的操作聚集在一起,调用者只需要面对一个对象,而不是一堆散落的函数
"""

# 析构函数:__del__()
# 删除对象的时候,解释器会默认调用__del__(方法)
# class Person:
#     def __init__(self):
#         print('我是__init__()')
#     def __del__(self):
#         print('被销毁了')
#     def pr(self,f=None):
#         print(666,f)

# p = Person()
# p.pr(777)

# del p       # 函数被删除时立即执行__del__,

# e = Person()
# e.pr(999)

"""
__del__是 Python 中的析构方法。在 CPython 解释器中，当一个对象的引用计数降为 0 时(或者更广义地说，
当垃圾回收器确定这个对象无法再被访问到时(,Python 会调用该对象的 __del__方法,然后释放对象占用的内存。
__del__并不是“所有实例方法执行完后的收尾工作”,而是“对象被销毁时的临终遗言”。只要对象还活着(被引用)
，即使它的方法早就执行完了,__del__也不会触发。
"""


"""
面向对象的三个特性:封装,继承,多态
"""


# 1.封装:隐藏对象中不希望被外部访问的属性或方法
# class Person:
#     name = 'zzw'
#     __age = 18      # 隐藏属性:  __属性名
#     def introduce(self):
#         print(f'{Person.name}的年龄是{Person.__age}')       # 在实例方法中访问类属性和隐藏属性

# p1 = Person()
# print(p1.name)

# # 隐藏属性,只允许在类的内部使用,无法通过对象访问
# # print(p1.__age)     # 无法访问__age

# # 隐藏属性实际上是将名字修改为:  _类名__属性名
# print(p1._Person__age)      # 可以访问__age

# p1.introduce()

# 1.xxx :普通属性/方法,可以正常访问
# 2._xxx :声明私有属性/方法,外部可以使用,之类也可以继承,但是在另一个py文件中,通过from xxx impot * 导入时,无法导入
# 3.__xxx :隐藏属性,无法在外部直接访问,子类不会继承,要访问只能通过间接的方式,另一个py文件中通过from xxx import * 也无法导入

# class Person:
#     name = 'zzw'
#     __age = 18
#     _sex = 'man'
#     def _fan1(self):
#         print(f'一个名为{self.name}的{self._sex}今年{self.__age}岁了')

# pe = Person()
# print(pe._sex)

# pe._fan1()


# 2.继承
# 就是让类与类之间转化为父子关系,之内默认继承父亲的属性和方法
# 语法:
# class 类名(父亲名):
#     代码块

# 2.1单继承
# class Fan:
#     a = '你真棒'
#     b = 666
#     def Fan1(self):
#         print(f'{self.a},{self.b}')

# class fan(Fan):         # 继承Fan的类属性和实例方法
#     c = '我真无敌'
#     d = 999
#     def fan1(self):
#         print(f'{self.c},{self.d}')

# class fan_1(fan):       # 继承的传递(多层继承),拥有fan和Fan的类属性和类方法
#     def Fan1(self):
#         print(f'{self.c},{self.d}')     # 子类可以自己定义父类的实例方法,但不会改变父类的实例方法

# F1 = Fan()
# f1 = fan()
# f1_1 = fan_1()

# print(F1.a)
# print(f1.a)
# f1.Fan1()      # 拥有父类的父类的......类方法和类属性
# f1_1.Fan1()     # 覆盖后就是自己的实例方法,调用时与父类无关


# F1.fan1()       # 父类不能调用子类的类属性和实例方法,结果会报错

# 2.2多继承
# class K1:
#     K_1 = 520
#     K_2 = 1314
#     def __init__(self):
#         print('我是父类K1中的__init__')
#     def _K1(self):
#         return '我是父类K1的实例方法'

# class K2:
#     K_3 = 250
#     def __init__(self):
#         print('我是父类K2中的__init__')
#     def _K2(self):
#         return '我是父类K2的实例方法'

# class k(K1,K2):     # MCO元组的顺序是k k1 k2
#     pass

# a = k()

# python使用C3线性化算法优化,为每个类生成了一个MRO元组,决定了方法的查找顺序
# 可以通过ClassNsme.__mro__ 查看

# print(a._K1(),a._K2())      # 由于 k 没有__init__ 所以按照顺序会调用 k1 的 __init__

# print(k.__mro__)

"""
super()就是严格按照这个顺序调用"下一个"类的方法
"""
class a:
    def __init__(self):
        print("a init")
        super().__init__()



class A:
    def __init__(self):
        print("A init")
        super().__init__()      # 要有括号
    
class B(A):
    def __init__(self):
        print("B init")
        super().__init__()

class C(a):
    def __init__(self):
        print("C init")
        super().__init__()
    
class D(C,B):       # MRO 的顺序是D　Ｂ　Ａ　Ｃ　ａ　；如果是Ｄ(C,B) 则顺序是　D C ａ　Ｂ　Ａ
    def __init__(self):
        print("D init")
        super().__init__()
        
d = D()





