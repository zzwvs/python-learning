class Pokemon:
    def __init__(self):
        self.name = '初级小精灵'     # 名称
        self.level = 0       # 等级
        self._energy = 100       # 体力
    def eat(self):      # 吃东西
        if self._energy + 20 > 100:
            self._energy = 100
            print('体力已满，无需回复')
        else:
            self._energy += 20
            print(f'已回复20体力,当前体力为{self._energy}')
            
    
    def train(self):    # 进行训练
        if self._energy - 30 < 0:
            print('体力不足')
            return
        else:
            self._energy -= 30
            if self.level < 20:
                self.level += 1
            elif self.level >= 20:
                print('20已满级')
                print('完成训练,已满级')
            print('已完成训练')
            

    def show_status(self):      # 查询当前状态
        if 5 <= self.level < 10:
            self.name = '中级小精灵'
        elif 10 <= self.level <15:
            self.name = '高级小精灵'
        elif 15 <= self.level <20:
            self.name = '顶级小精灵'
        elif self.level >= 20:
            self.name = '满级小精灵'
        print(self.name)
        print(f'精灵等级为{self.level}')
        print(f'当前体力为{self._energy}')
        


p1 = Pokemon()  # 1号小精灵
p2 = Pokemon()  # 2号小精灵

def main():
    while True:
        print('你获得了两个小精灵，你是否愿意培养她们')
        print('愿意(输入"y"),不愿意(输入"n")')
        u = input().strip()
        if u == 'n':
            print('---你错过了小精灵😭😭😭---')
            return
        elif u != 'y' and u != 'n':
            print('请重新输入')
            continue
        elif u == 'y':
            print('---恭喜你获得了小精灵🎉---')
            break
    while True:
        s = input('请选择你要培养几号小精灵').strip()
        if s not in ['1','2']:
            print('请重新输入')
            continue
        elif s == '1':
            P = p1
        elif s == '2':
            P = p2
        print('-----你要执行一下那些操作-----')
        print('-----1.吃东西-----')
        print('-----2.进行训练-----')
        print('-----3.查询当前状态-----')
        print('-----请输入对应的数字-----')
        c = input().strip()
        if c not in ['1','2','3']:
            print('请重新输入')
            continue
        # elif c == '1':
        #     P.eat()
        # elif c == '2':
        #     P.train()
        # elif c == '3':
        #     P.show_status()
        else:
            f = {'1':P.eat,'2':P.train,'3':P.show_status}[c]
            f()
                
                
                
if __name__ == '__main__':
    main()
        


            