# #1.
# sums = [1,2,3,4,5,6,7,8,9,10]
# sums_int = [x for x in sums if x % 2 == 0]      #只有一个if就写在最后
# print(sums_int)
# #2.
# names = ['alice','BOB','Charlie','dAvId']
# new_names = [name.strip().title() for name in names]        #前面执行的操作,后面遍历整个列表
# print(new_names)
# #3.
# nums = [1,2,3,4,5]
# new_nums = [ num * 2 if num % 2 == 0 else num ** 2 for num in nums ]        #有else或elif就写开头,开头写操作不写if
# print(new_nums)
# #4.
# list1 = ["A", "B"]      
# list2 = [1, 2, 3]
# new_list = []
# for i in list1:
#     for x in list2:
#         a = (i,x)
#         new_list.append(a)
# print(new_list)

# b = [(x,y) for x in list1 for y in list2]
# print(b)
# #5.
# 1. 初始化游戏状态
ships_left = 3
cities_left = 5
player_energy = 10

# 设置一个标志变量，作为程序运行的“总开关”
game_is_active = True

# 2. while循环只检查这一个简单条件
def 游戏():
    while game_is_active:
        print(f"飞船:{ships_left}, 城市:{cities_left}, 能量:{player_energy}")

        # 3. 在循环内部，检查各种复杂的失败条件
        if ships_left <= 0:
            print("警报：飞船全部损毁！")
            game_is_active = False  # 关闭总开关
        elif cities_left <= 0:
            print("遗憾：城市全部沦陷！")
            game_is_active = False  # 关闭总开关
        elif player_energy <= 0:
            print("警告：能量耗尽！")
            game_is_active = False  # 关闭总开关
        else:
            # 如果没有触发失败，正常进行游戏
            ships_left -= 1
            cities_left -= 1
            player_energy -= 2

    # 4. 循环结束后的统一处理
    print("游戏结束，感谢游玩。")

游戏()
