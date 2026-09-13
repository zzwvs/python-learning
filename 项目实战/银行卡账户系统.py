class BankAccount:
    def __init__(self,holder,password):
        self.account_holder = holder    # 持卡人
        self.__password = password    # 密码
        self.__balance = 0   # 初始金额
        self.transaction_log = []    # 交易记录
    
    def deposit(self):    # 存款
        m = input("请输入密码:").strip()
        if m == str(self.__password):
            while True:
                try:
                    amout = input("存入的金额是:")
                    amout = int(amout)
                    break
                except ValueError:
                    print("输入错误,请重新输入❌")
                
            self.__balance = self.__balance + amout
            self.transaction_log.append(f"存入{amout}")
            print(f"你已存入{amout}元")
        else:
            print("密码验证失败,已退回")
            return

    def withdraw(self):     # 取款
        m = input("请输入密码:").strip()
        if m == str(self.__password):
            while True:
                try:
                    amout = input("取出的金额是:")
                    amout = int(amout)
                    if amout > self.__balance:
                        print("余额不足")
                        continue
                    else:
                        break
                except ValueError:
                    print("输入错误,请重新输入❌")
                
            self.__balance = self.__balance - amout
            self.transaction_log.append(f"取出{amout}")
            print(f"你已取出{amout}元")
        else:
            print("密码验证失败,已退回")
            return

    def check_balance(self):    # 查询余额
        m = input("请输入密码:").strip()
        if m == str(self.__password):
            print(f"当前余额:{self.__balance}")
        else:
            print("密码验证失败,已退回")

    def change_password(self):      # 修改密码
        m = input("请输入密码:").strip()
        if m == str(self.__password):
            while True:
                new = input("请输入新密码:")
                try:
                    new = int(new)
                    break
                except ValueError:
                    print("请输入正确的密码")
            self.__password = new
        else:
            print("验证失败,已退回")
            return
    
    def show_transaction_log(self):     # 查询所有交易记录
        print(f"持卡人:{self.account_holder}:")
        print("======交易记录=====")
        for i in self.transaction_log:
            print(i)
        print("==================")


def main():
    name = input("请输入你的持卡人姓名:")
    while True:
        mima = input("请输入你的密码:")
        try:
            mima = int(mima)
        except ValueError:
            print("密码必须是整数")
            continue
        B = BankAccount(name,mima)
        break
    while True:
        print("请选择你的操作")
        print("============")
        print("1.存款")
        print("2.取款")
        print("3.查询余额")
        print("4.修改密码")
        print("5.查询所有交易记录")
        print("============")
        i = input()
        f = {'1':B.deposit,'2':B.withdraw,'3':B.check_balance,'4':B.change_password,'5':B.show_transaction_log}[i]
        f()


if __name__ == "__main__":
    main()
