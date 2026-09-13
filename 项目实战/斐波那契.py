
# def fan1(n):
#     if n <= 1:     
#         return 1
#     else:
#         return fan1(n-1) + fan1(n-2)

# def fan_1(n):
#     fn = []
#     for i in range(1,n+1):
#         fn.append(fan1(i))
#     print(fn)



from functools import reduce

# def fib_reduce(n: int):
#     if n <= 0:
#         return []
#     # 初始累加器为 [0, 1]，每次迭代在后面追加上一个数
#     result = reduce(
#         lambda acc, _: acc + [acc[-1] + acc[-2]],
#         range(n - 2),  # 因为初始已有2个数，只需迭代 n-2 次
#         [0, 1]
#     )
#     return result[:n]  # 防止 n=1 时多出多余的 1

# print(fib_reduce(10))
# # 输出: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]



def add(e):
    ad = []
    y = lambda a,b: a + b
    n = 1
    while True:
        s = range(n)
        x = reduce(y,s)
        ad.append(x)
        n = n + 1
        e = e - 1
        if e == 0:
            break
    print(ad)


add(15)




