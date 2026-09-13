import random

def sjs(x):
    偶数 = 0
    奇数 = 0
    n = 0
    v = x
    while True:
        i = random.randint(1,100)
        if i % 2 == 0:
            偶数 += 1
        elif i % 2 == 1:
            奇数 += 1
        n += 1
        v -= 1
        if v <= 0:
            break
    return 偶数,奇数,n
    

def pr(x):
    z,c,n = sjs(x)
    ou = z/n
    ji = c/n
    return ou,ji

def ru():
    统计 = {}
    ji = []
    ou = []
    for _ in range(101):
        x,y = pr(100)
        ou.append(x)
        ji.append(y)
        统计['偶数'] = ou
        统计['奇数'] = ji
    return 统计

k = ru()
print(k)
print(f'奇数最大值为{max(k['奇数']):.2%}')
print(f'偶数最大值为{max(k['偶数']):.2%}')

    
    
    


    

