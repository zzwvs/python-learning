import random

# ==================== 面向对象核心 ====================

class Character:
    """角色基类（封装）"""
    def __init__(self, name, hp, attack_power):
        self.name = name
        self._hp = hp          # 受保护属性，不能直接乱改
        self.max_hp = hp
        self.attack_power = attack_power

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, value)  # 血量最低为0，防止出现负数

    def is_alive(self):
        return self._hp > 0

    def basic_attack(self, target):
        # 随机浮动伤害，更有游戏感
        damage = random.randint(self.attack_power - 2, self.attack_power + 2)
        target.take_damage(damage)
        return damage

    def take_damage(self, damage):
        self._hp -= damage
        print(f'  ➜ {self.name} 受到了 {damage} 点伤害！')

    def show_status(self):
        # 简单画个血条
        bar = '❤️' * (self._hp // 10) + '🖤' * ((self.max_hp - self._hp) // 10)
        print(f'  【{self.name}】 {bar} {self._hp}/{self.max_hp}')


class Player(Character):
    """玩家类（继承 Character）"""
    def __init__(self, name):
        super().__init__(name, hp=100, attack_power=15)
        self.potions = 2  # 玩家特有属性：药水

    def heavy_strike(self, target):
        """重击技能（伤害更高）"""
        damage = random.randint(self.attack_power + 5, self.attack_power + 10)
        target.take_damage(damage)
        print(f'  🗡️ 你使用了【重击】，造成了 {damage} 点伤害！')

    def heal(self):
        """喝药回血"""
        if self.potions > 0:
            self.potions -= 1
            self.hp += 30
            print(f'  🧪 你喝下了药水，回复了 30 点 HP！(剩余药水: {self.potions})')
        else:
            print('  ❌ 没有药水了！')


class Boss(Character):
    """Boss类（继承 Character，并重写方法实现多态）"""
    def __init__(self):
        super().__init__('暗黑魔龙', hp=200, attack_power=12)
        self.phase = 1  # Boss 有阶段概念

    def take_damage(self, damage):
        """多态：重写受伤方法，血量低时触发狂暴"""
        self._hp -= damage
        print(f'  🐉 {self.name} 受到了 {damage} 点伤害！')
        
        # 狂暴机制：血量低于一半时攻击力暴涨
        if self.phase == 1 and self._hp < self.max_hp / 2:
            self.phase = 2
            self.attack_power += 10
            print(f'  🔥 >>> {self.name} 狂暴了！攻击力提升至 {self.attack_power}！<<<')

    def special_attack(self, target):
        """Boss 特有技能"""
        print(f'  🔥 {self.name} 使用了【烈焰吐息】！')
        damage = random.randint(self.attack_power, self.attack_power + 12)
        target.take_damage(damage)


# ==================== 游戏主循环 ====================

def battle():
    p = Player('勇敢的Pythoner')
    b = Boss()

    print('=' * 40)
    print('  🐉 欢迎来到大BOSS挑战！ 🐉')
    print('=' * 40)
    p.show_status()
    b.show_status()

    # 战斗循环
    while p.is_alive() and b.is_alive():
        print('\n--- 你的回合 ---')
        print('  1. 普通攻击   2. 重击   3. 喝药')
        choice = input('  请选择行动 (输入数字)：').strip()

        if choice == '1':
            p.basic_attack(b)
        elif choice == '2':
            p.heavy_strike(b)
        elif choice == '3':
            p.heal()
        else:
            print('  ❌ 慌乱中你错过了机会！')

        # Boss 反击
        if b.is_alive():
            print('\n--- 敌人回合 ---')
            # 狂暴阶段有40%概率放特殊技能
            if b.phase == 2 and random.random() < 0.4:
                b.special_attack(p)
            else:
                b.basic_attack(p)

        # 显示状态
        p.show_status()
        b.show_status()

    # 战斗结束
    print('\n' + '=' * 40)
    if p.is_alive():
        print('  🎉 恭喜你！你击败了大BOSS，证明了你的OOP实力！')
    else:
        print('  💀 你倒下了...不过没关系，调整代码再战！')
    print('=' * 40)


if __name__ == '__main__':
    battle()