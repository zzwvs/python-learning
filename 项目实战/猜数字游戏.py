import random

is_pro = True
record = []
attempts_left = 0       # 模块级变量,跨函数调用保持状态

def randoms(n):         # 随机数成器
    num = random.randrange(1,n+1)
    return num,n



def Difficulty():
    i = error()
    return i



def error():
    while True:
        s = input('1.简单\n2.普通\n3.困难\n4.退出')
        try:
            v = int(s)
        except Exception:
            print('请输入整数')
            continue

        if not 1 <= v <= 4:
            print('请输入1-4中的数字')
            continue
        else:
            break
    return v



def process():      # 主进程
    global attempts_left
    i = Difficulty()
    if i == 4:
        return
    range_map = {1:50,2:100,3:200}
    x = range_map[i]
    num,n = randoms(x)
    attempts_left = {50:10,100:7,200:5}[n]      # 初始化剩余次数,每次新游戏重置
    while is_pro:
        q = input('输入你的数字:')
        try:
            e = int(q)
        except Exception:
            print('请输入整数')
        
        if not 1 <= e <= n:
            print(f'请输入1-{n}的整数')
        else:
            attempts_left = attempts_left - 1
            if e > num:
                print('数字大了,请继续')
                collect(q,'数字大了')
                if attempts_left == 0:
                    print('次数已用完,游戏结束')
                    counter()
                    break
                continue
            elif e < num:
                print('数字小了,请继续')
                collect(q,'数字小了')
                if attempts_left == 0:
                    print('次数已用完,游戏结束')
                    counter()
                    break
                continue
            elif e == num:
                collect(q,'猜对了')
                print('猜对了')
                counter()
    print(collect())


def counter():     # 计步器
    global is_pro
    is_pro = False






def collect(m=None,l=None):         # 存储历史记录
    record.append({m:l})
    return record


if __name__ == '__main__':
    process()




