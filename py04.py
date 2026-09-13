'''
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name} 
    return person 
musician = build_person('jimi', 'hendrix')
print(musician)
'''
"""
# 不需要先创建巨大的数字列表，直接用 range 对象即可（它本身就是惰性的）
def get_odds(n):
    # 使用 yield 关键字，这就变成了一个生成器
    for i in range(1, n):
        if i % 2 != 0:
            yield i

# 调用
gen = get_odds(1000000)

# 打印时需要注意,print(gen) 只会打印对象地址
# 你需要遍历它才能看到数字，或者取前几个看看
for num in gen:
    print(num) 
    # 如果只想看前几个，可以加个计数器 break 掉
"""
# from pickletools import float8

# import numpy as np
# p = float(input('请输入0-1000中的数字数字:'))
# 幂 = float(input('你要开几次方根:'))
# def 平方根运算():
#     b = float('inf')
    
#     for i in np.arange(0,1000.001,0.001):
#         a = abs(p - float(i**幂))
#         if a < b:
#             b = a
#             m = i
#     print(m)

# 平方根运算()

l = {'a':1,'b':2,'c':3,'d':2,'e':3}
a = dict()
b = set()
def 去除字典中重复的值():
    for key,value in l.items():
        if value not in b:
            a[key] = value
            b.add(value)
    print(a)
            
去除字典中重复的值()










