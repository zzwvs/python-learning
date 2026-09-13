user = {}       # 创建学生信息字典

def add():      # 添加信息
    information = {}

    while True:
        
        while True:
            ID = input('请输入学生学号:')
            if not ID.isdigit():        # .isdigit()可以判断字符串是否只包含数字
                print('输入有误,请重新输入')
                continue
            else:
                ID = int(ID)        # 转化为整数
                break
                
        name = input('请输入学生姓名:')
        while True:
            grades_chinese = input('请输入学生语文成绩:')
            grades_math = input('请输入学生数学成绩:')
            grades_english = input('请输入学生的英语成绩:')
            try:
                grades_chinese = float(grades_chinese)
                grades_math = float(grades_math)
                grades_english = float(grades_english)
                break
            except ValueError:
                print('输入有误,请重新输入')
                continue

        information['学号'] = ID
        information['chinese'] = grades_chinese
        information['math'] = grades_math
        information['english'] = grades_english
        user[name] = information


        is_add = input('继续添加(输入1),终止添加(输入2):')
            
        if int(is_add) == 1:
            continue
        elif int(is_add) == 2:
            break
        else:
            print('输入有误,请重新输入:')
            
            
        



def dels():         # 删除信息
    while True:
        del_name = input('请输入你要删除学生信息的姓名:')
        try:
            del user[del_name]
            print('已删除')
        except KeyError:
            print('请核对你输入的学生姓名')
            continue
        break



def modify():       # 修改成绩
    while True:
        name = input('请输入你要更改成绩的学生:')
        if name not in user:
            print('查无此人,请重新输入')
        else:
            while True:
                subject = input('请输入你要更改的科目(语文输入1,数学输入2,英语输入3,不修改输入4):')
                if int(subject) == 1:
                    sub = 'chinese'
                    break
                elif int(subject) == 2:
                    sub = 'math'
                    break
                elif int(subject) == 3:
                    sub = 'english'
                    break
                elif int(subject) == 4:
                    return
                
                    
        number = input('请输入更改后的成绩:')
        user[name][sub] = float(number)
        print('以完成修改')
        return
        



def check():        # 查询单个学生信息
    name = input('请输入你要查询的学生姓名:')
    try:
        summarize = (user[name]['chinese'] + user[name]['math'] + user[name]['english'])
        print(user[name])
        print(f'平均分:{summarize/3}')
    except KeyError:
        print('请核对你输入的学生姓名')



# def sort():         # 显示所有学生信息
#     if not user:
#         print('没有学生信息')
#         return
#     students = []
#     for name in user:
#         total = (user[name]['chinese'] + user[name]['math'] + user[name]['english'])
#         students.append({name:total})
#     sorted_users = sorted(students,key=lambda x: x['total'])
#     print(sorted_users)


def sort():
    if not user:
        print('没有学生信息')
        return

    students = []
    for name in user:
        info = user[name]
        total = info['chinese'] + info['math'] + info['english']
        students.append({
            'name': name,
            'total': total,
            'chinese': info['chinese'],
            'math': info['math'],
            'english': info['english'],
        })

    sorted_users = sorted(students, key=lambda x: x['total'], reverse=True)

    print('按总分排序如下：')
    for s in sorted_users:
        print(f"{s['name']} 总分:{s['total']} 语文:{s['chinese']} 数学:{s['math']} 英语:{s['english']}")











def sta():      # 各科统计
    chinese_sort = []
    math_sort = []
    english_sort = []
    if user == {}:
        print('尚未添加学生')
    else:
        for name in user:
            chinese_sort.append(user[name]['chinese'])
            math_sort.append(user[name]['math'])
            english_sort.append(user[name]['english'])
    print(f'语文平均分:{sum(chinese_sort)/len(user)}  数学平均分:{sum(math_sort)/len(user)}   英语平均分:{sum(english_sort)/len(user)}')
    print(f'语文最高分:{max(chinese_sort)}  最低分{min(chinese_sort)}')
    print(f'数学最高分:{max(math_sort)}  最低分{min(math_sort)}')
    print(f'英语最高分{max(english_sort)}  最低分{min(english_sort)}')




while True:
    Choose = input('请选择你要执行的操作(1.添加学生,2.删除学生,3.修改成绩,\n4.查询单个学生信息,5.显示所有学生信息,\n6.统计各科平均分、最高分、最低分7.退出程序)')
    try:
        if int(Choose) == 1:
            add()
        elif int(Choose) == 2:
            dels()
        elif int(Choose) == 3:
            modify()
        elif int(Choose) == 4:
            check()
        elif int(Choose) == 5:
            sort()
        elif int(Choose) == 6:
            sta()
        elif int(Choose) == 7:
            break
        else:
            print('请输入有效数字')
            continue
    except Exception as e:
        print(e)
        
    
        



















