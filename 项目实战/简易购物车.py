product_list = {}

is_pro = True

products = [{'id':1,'name':'苹果🍎','price':20},
            {'id':2,'name':'铅笔✏','price':5},
            {'id':3,'name':'橡皮擦','price':6},
            {'id':4,'name':'巧克力🍫','price':50},
            {'id':5,'name':'蛋糕🎂','price':100}
]



def acc():
    u = input('输入你的账户名')
    return u


def pre():
    u = [acc()]
    product_list.append(u)
    while is_pro:
        print("以下是商品预览\nid:1 name:苹果🍎,price:20\nid:2 name:铅笔铅笔✏ price:5\nid:3 name:橡皮擦 price:6 \nid:4 name:巧克力🍫 price:50\nid:5 name:蛋糕🎂 price:100")
        s = input('请输入编号选择你要购买的商品:')
        
        try:
            n = int(s)
            if not 1 <= n <= 5:
                print('请输入已有的商品编号')
                continue
            else:
                while True:
                    i = input('是否继续买入?(y/n)')
                    if i == 'y':
                        count(n)
                        break
                    elif i == 'n':

                        break
                    else:
                        print('请输入正确的回答')
                        continue
            continue

        except ValueError:
            print('请输入正确的数字')
            continue




def count(m,x=0):
    while True:
        mun = input('你要购买多少份:')
        try:
            mun = int(mun)
        except ValueError:
            print('请输入正确的数字')
            continue
        product_list[x].append({'数量':mun})
        product_list[x].append(products[m-1])
        
        print('已帮你存入购物箱')
        while True:
            t = input('还需要购买其他商品吗?(y/n):')
            if t == 'y':
                global is_pro
                is_pro = True
                break
            elif t == 'n':
                is_pro = False
                break
            else:
                print('请输入正确的回答')
                continue
        break
        

        

def sta():
    print('以下统计了你的购物信息,请核对')
    print(product_list)
    
    




if __name__ == '__main__':
    pre()
    sta()




