preview = {}        # 所有用户总购物车预览

users = dict()
user = {}           # 每个用户的购物车详细

products = [        # 商品列表
    {"id": 1, "name": "苹果",   "price": 5.5},
    {"id": 2, "name": "铅笔",   "price": 2.0},
    {"id": 3, "name": "橡皮擦", "price": 1.5},
    {"id": 4, "name": "巧克力", "price": 15.0},
    {"id": 5, "name": "蛋糕",   "price": 30.0},
]


def user_log_in():      # 用户登录
    e = input('         请输入里的用户名        ')
    if e.strip() == '':
        print('     用户名不能为空      ')
        return
    else:
        return e        # add()的实参






def look():
    print('                       预览商品                            ')
    print('==========================================================')
    for i in products:
        print(f'编号{i['id']}    名称:{i['name']}    单价:{i['price']}')



def add(us='游客'):          # 添加商品到购物车
    if users == dict():
        us = '游客'
    i = input('     输入你要添加的商品编号      ')
    # 形参us的实参是返回值e
    try:
        i = int(i)
        s = list()
        for x in products:
            s.append(x['id'])
            if x['id'] == i:
                n = x['name']
                num = x['price']
        if i not in s:
            print('     请输入正确的编号        ')
            n = None
            num = None
            return
    except Exception:
        print('     请输入正确的数字        ')
        return

    m = input(      '输入你要购买的数量     ')
    try:
        m = int(m)
    except Exception:
        print('     请输入正确的数字        ')
        return

    if n in user.values():
        user["数量"] = user["数量"] + m
        user['总价'] = user['数量'] * user['单价']
    else:
        user['编号'] = i
        user['数量'] = m
        user['单价'] = num
        user['总价'] = m*num

    users[n] = user

    preview[us] = users




def check():        # 查看购物车
    try:
        for x,i in users.items():
            print(f'商品名:{x} 单价:{i['单价']} 数量:{i['数量']} 小计:{i['总价']}')
    except KeyError:
        print('     购物车还没有收入商品        ')
        return
    
    
    
    
    
def modify():       # 修改购物车
    if preview == {}:
        print('     购物车为空,无法修改     ')
        return
    print('     输入你要修改的商品编号      ')
    x = input()
    try:
        x = int(x)
    except Exception:
        print('     请输入正确的数字        ')
        return
    print('     请输入修改后的数量      ')
    m = input()
    try:
        m = int(m)
    except Exception:
        print('     请输入正确的数字        ')
        return

    for p in preview.values():
        if x == p['编号']:
            p['数量'] = m
            p['总价'] = p['数量'] * p['单价']
    
    print('修改成功')



def del_():         # 删除某件商品
    print('     输入你要删除的商品编号      ')
    d = input()
    try:
        d = int(d)
    except Exception:
        print('     请输入正确的数字        ')
        return
    v = list()
    for i in users.values:
        v.append(i['编号'])
        if d not in v:
            print('     该用户没有收录该商品        ')
            return
        else:
            if d == i['编号']:
                del users[{1:'苹果',2:'铅笔',3:'橡皮',4:'巧克力',5:'蛋糕'}[d]]


            



def sett():         # 结算
    try:
        global preview,users
        print(f'商品总价为{user["总价"]}')
        print(f'已结算{user["总价"]}')
        print('购物车以清空')
        print('欢迎下次光临')
        preview = {}        
        user = {}
    except KeyError:
        print('     购物车为空,无法结算')
        return




if __name__ == '__main__':
    while True:
        print('=============================')
        print('     请输入你要执行的操作        ')
        print('1.用户登录')
        print('2.查看购物车')
        print('3.添加商品到购物车')
        print('4.修改购物车')
        print('5.删除某件商品')
        print('6.结算')
        print('7.退出程序')
        v = input()
        try:
            v = int(v)
        except Exception:
            print('请输入正确的数字')
        
        if v == 1:
            e = user_log_in()
        elif v == 2:
            check()
        elif v == 3:
            add(e)
        elif v == 4:
            modify()
        elif v == 5:
            del_()
        elif v == 6:
            sett()
        elif v == 7:
            print('退出程序,再见')
            break
        else:
            print("❌ 无效的编号，请输入 1-7")
            continue
        
    






