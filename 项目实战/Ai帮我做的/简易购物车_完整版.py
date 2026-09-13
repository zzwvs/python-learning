# ============================================================
# 简易购物车小程序（完整版，对照题目要求逐条实现）
# 项目二：简易购物车程序
# ============================================================
import sys
import io

# Windows 控制台默认用 GBK，打印 emoji 会报错，这里统一改成 UTF-8 输出
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ---------- 1. 预定义商品列表（至少5个商品） ----------
products = [
    {"id": 1, "name": "苹果",   "price": 5.5},
    {"id": 2, "name": "铅笔",   "price": 2.0},
    {"id": 3, "name": "橡皮擦", "price": 1.5},
    {"id": 4, "name": "巧克力", "price": 15.0},
    {"id": 5, "name": "蛋糕",   "price": 30.0},
]

# ---------- 2. 购物车用字典保存：{用户名: {商品编号: 数量}} ----------
carts = {}          # 每一位用户都有自己的字典购物车
current_user = None # 当前登录的用户名


def find_product(pid):
    """按商品编号查找商品，找不到返回 None"""
    for p in products:
        if p["id"] == pid:
            return p
    return None


def login():
    """用户登录：无需验证，直接输入用户名即可"""
    global current_user
    name = input("请输入你的用户名: ").strip()
    # 用三目运算给个默认值：名字为空时用"游客"代替
    name = name if name else "游客"
    if name not in carts:
        carts[name] = {}                # 给新用户创建空购物车
    current_user = name
    print(f"✅ 欢迎 {name}！你的购物车已就绪\n")


def show_menu():
    """主菜单"""
    print("========== 简易购物车 ==========")
    print(" 1. 浏览商品")
    print(" 2. 添加商品到购物车")
    print(" 3. 查看购物车")
    print(" 4. 修改购物车中某商品数量")
    print(" 5. 删除购物车中某商品")
    print(" 6. 结算")
    print(" 7. 退出")
    print("================================")


def show_products():
    """1. 浏览商品：显示所有商品编号、名称、单价"""
    print("\n--- 商品列表 ---")
    for p in products:
        print(f"编号:{p['id']}  名称:{p['name']}  单价:{p['price']}元")


def add_to_cart():
    """2. 添加商品到购物车（已有该商品则累加数量）"""
    show_products()
    pid = input("请输入要加入购物车的商品编号: ")
    if not pid.isdigit():
        print("❌ 请输入数字")
        return
    pid = int(pid)

    p = find_product(pid)
    if p is None:
        print("❌ 没有这个商品")
        return

    qty = input("请输入数量: ")
    if not qty.isdigit() or int(qty) <= 0:
        print("❌ 请输入正整数")
        return
    qty = int(qty)

    cart = carts[current_user]
    # 关键点：字典 get(pid, 0) 已存在就取原数量，不存在就按 0 算，然后累加
    cart[pid] = cart.get(pid, 0) + qty
    print(f"✅ 已加入购物车：{p['name']} {qty} 件")


def view_cart():
    """3. 查看购物车：显示商品名、单价、数量、小计，并计算总价"""
    cart = carts[current_user]
    if not cart:
        print("你的购物车是空的")
        return

    print("\n--- 我的购物车 ---")
    # 用 lambda + sum 计算总价（题目要求：total = sum(...)）
    total = sum(map(lambda pid: find_product(pid)["price"] * cart[pid], cart))

    for pid, qty in cart.items():
        p = find_product(pid)
        subtotal = p["price"] * qty
        print(f"{p['name']}  单价:{p['price']}元  数量:{qty}  小计:{subtotal}元")
    print(f"合计: {total}元")


def update_qty():
    """4. 修改购物车中某商品数量"""
    cart = carts[current_user]
    pid = input("请输入要修改数量的商品编号: ")
    if not pid.isdigit():
        print("❌ 请输入数字")
        return
    pid = int(pid)

    if pid not in cart:
        print("❌ 购物车中没有这个商品")
        return

    qty = input("请输入新的数量: ")
    if not qty.isdigit() or int(qty) <= 0:
        print("❌ 请输入正整数")
        return
    cart[pid] = int(qty)
    print("✅ 修改成功")


def remove_item():
    """5. 删除购物车中某商品"""
    cart = carts[current_user]
    pid = input("请输入要删除的商品编号: ")
    if not pid.isdigit():
        print("❌ 请输入数字")
        return
    pid = int(pid)

    if pid in cart:
        del cart[pid]
        print("✅ 已删除")
    else:
        print("❌ 购物车中没有这个商品")


def checkout(**kwargs):
    """6. 结算：计算总价并清空购物车
    用 **kwargs 接收额外参数，例如 checkout(discount=0.9) 表示打9折"""
    cart = carts[current_user]
    if not cart:
        print("购物车是空的，无法结算")
        return

    discount = kwargs.get("discount", 1.0)  # 默认不打折

    total = sum(map(lambda pid: find_product(pid)["price"] * cart[pid], cart))
    final_total = total * discount

    print(f"\n商品总价: {total}元")
    print(f"折扣: {discount}" if discount != 1.0 else "今日无折扣")
    # 三目运算示例
    print(f"应付金额: {final_total}元" if discount == 1.0 else f"折后应付: {final_total}元")

    cart.clear()             # 清空购物车
    print("✅ 结算完成，购物车已清空")


def main():
    """主入口：登录后进入持续交互菜单"""
    login()
    while True:
        show_menu()
        choice = input("请输入功能编号(1-7): ")

        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            update_qty()
        elif choice == "5":
            remove_item()
        elif choice == "6":
            checkout(discount=0.9)   # 演示：结算时传一个9折的额外参数
        elif choice == "7":
            print("👋 退出程序，再见！")
            break
        else:
            print("❌ 无效的编号，请输入 1-7")


if __name__ == "__main__":
    main()
