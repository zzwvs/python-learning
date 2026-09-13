# -*- coding: utf-8 -*-
# 学生成绩管理系统（修改版）
# 说明：
# 1. 使用「学号」作为唯一标识，避免同名学生互相覆盖，减少信息混乱。
# 2. 修复了原 sort() 函数中的格式化与排序错误。
# 3. 修复了 sta() 在没有学生时可能崩溃的问题。
# 4. 增加输入校验，避免非法学号/成绩导致程序异常。

students = {}  # 学号(int) -> {'姓名': str, '语文': float, '数学': float, '英语': float}


def input_student_id():
    """输入一个不重复的纯数字学号。"""
    while True:
        s = input('请输入学生学号（纯数字）: ').strip()
        if not s.isdigit():
            print('输入有误，学号必须是纯数字，请重新输入')
            continue
        uid = int(s)
        if uid in students:
            print(f'学号 {uid} 已存在，请重新输入')
            continue
        return uid


def input_student_name():
    """输入非空的学生姓名。"""
    while True:
        name = input('请输入学生姓名: ').strip()
        if name:
            return name
        print('姓名不能为空，请重新输入')


def input_grade(subject_name):
    """输入一个合法的数字成绩。"""
    while True:
        s = input(f'请输入学生{subject_name}成绩: ').strip()
        try:
            value = float(s)
            return value
        except ValueError:
            print('输入有误，成绩必须是数字，请重新输入')


def add():
    """添加学生信息。"""
    while True:
        print('\n--- 添加学生信息 ---')
        uid = input_student_id()
        name = input_student_name()
        chinese = input_grade('语文')
        math = input_grade('数学')
        english = input_grade('英语')

        students[uid] = {
            '姓名': name,
            '语文': chinese,
            '数学': math,
            '英语': english,
        }
        print(f'已添加：学号 {uid}，姓名 {name}，语文 {chinese}，数学 {math}，英语 {english}')

        while True:
            is_add = input('继续添加(输入1)，终止添加(输入2): ').strip()
            if is_add == '1':
                break
            elif is_add == '2':
                return
            print('输入有误，请输入 1 或 2')


def dels():
    """按学号删除学生信息。"""
    if not students:
        print('没有学生信息')
        return

    while True:
        s = input('请输入要删除的学生学号: ').strip()
        if not s.isdigit():
            print('学号必须是纯数字，请重新输入')
            continue
        uid = int(s)
        if uid not in students:
            print('查无此学号，请重新输入')
            continue

        name = students[uid]['姓名']
        del students[uid]
        print(f'已删除学生：学号 {uid}，姓名 {name}')
        return


def modify():
    """按学号修改学生成绩。"""
    if not students:
        print('没有学生信息')
        return

    while True:
        s = input('请输入要修改成绩的学生学号: ').strip()
        if not s.isdigit():
            print('学号必须是纯数字，请重新输入')
            continue
        uid = int(s)
        if uid not in students:
            print('查无此学号，请重新输入')
            continue

        name = students[uid]['姓名']
        print(f'当前学生：学号 {uid}，姓名 {name}')

        while True:
            subject = input('请输入要更改的科目(语文输入1，数学输入2，英语输入3，不修改输入4): ').strip()
            if subject == '1':
                key = '语文'
                break
            elif subject == '2':
                key = '数学'
                break
            elif subject == '3':
                key = '英语'
                break
            elif subject == '4':
                return
            print('输入有误，请输入 1~4')

        new_score = input_grade(key)
        students[uid][key] = new_score
        print(f'已完成修改：{name}的{key}成绩改为 {new_score}')
        return


def check():
    """按学号查询单个学生信息。"""
    if not students:
        print('没有学生信息')
        return

    while True:
        s = input('请输入要查询的学生学号: ').strip()
        if not s.isdigit():
            print('学号必须是纯数字，请重新输入')
            continue
        uid = int(s)
        if uid not in students:
            print('查无此学号，请重新输入')
            continue
        break

    info = students[uid]
    total = info['语文'] + info['数学'] + info['英语']
    print('\n--- 学生信息 ---')
    print(f'学号: {uid}')
    print(f'姓名: {info["姓名"]}')
    print(f'语文: {info["语文"]}  数学: {info["数学"]}  英语: {info["英语"]}')
    print(f'总分: {total}  平均分: {total / 3:.2f}')


def sort():
    """显示所有学生信息，并按总分从高到低排序。"""
    if not students:
        print('没有学生信息')
        return

    records = []
    for uid, info in students.items():
        total = info['语文'] + info['数学'] + info['英语']
        records.append({
            '学号': uid,
            '姓名': info['姓名'],
            '语文': info['语文'],
            '数学': info['数学'],
            '英语': info['英语'],
            '总分': total,
        })

    sorted_records = sorted(records, key=lambda r: r['总分'], reverse=True)

    print('\n--- 所有学生信息（按总分从高到低）---')
    print(f"{'学号':<10}{'姓名':<10}{'语文':<8}{'数学':<8}{'英语':<8}{'总分':<8}{'平均分':<8}")
    for r in sorted_records:
        avg = r['总分'] / 3
        print(f"{r['学号']:<10}{r['姓名']:<10}{r['语文']:<8.1f}{r['数学']:<8.1f}{r['英语']:<8.1f}{r['总分']:<8.1f}{avg:<8.2f}")


def sta():
    """统计各科平均分、最高分、最低分。"""
    if not students:
        print('尚未添加学生')
        return

    chinese_list = [info['语文'] for info in students.values()]
    math_list = [info['数学'] for info in students.values()]
    english_list = [info['英语'] for info in students.values()]

    print('\n--- 各科统计 ---')
    print(f'语文平均分:{sum(chinese_list) / len(chinese_list):.2f}  '
          f'数学平均分:{sum(math_list) / len(math_list):.2f}  '
          f'英语平均分:{sum(english_list) / len(english_list):.2f}')
    print(f'语文最高分:{max(chinese_list)}  最低分:{min(chinese_list)}')
    print(f'数学最高分:{max(math_list)}  最低分:{min(math_list)}')
    print(f'英语最高分:{max(english_list)}  最低分:{min(english_list)}')


def main():
    """主菜单。"""
    while True:
        print('\n请选择你要执行的操作：')
        print('1. 添加学生')
        print('2. 删除学生')
        print('3. 修改成绩')
        print('4. 查询单个学生信息')
        print('5. 显示所有学生信息（按总分排序）')
        print('6. 统计各科平均分、最高分、最低分')
        print('7. 退出程序')

        choice = input('请输入选项(1~7): ').strip()
        if choice == '1':
            add()
        elif choice == '2':
            dels()
        elif choice == '3':
            modify()
        elif choice == '4':
            check()
        elif choice == '5':
            sort()
        elif choice == '6':
            sta()
        elif choice == '7':
            print('已退出程序')
            break
        else:
            print('请输入有效数字 1~7')


if __name__ == '__main__':
    main()
