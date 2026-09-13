
# """"

class Shape:    # 形状
    def __init__(self,name):
        self.name = name
        
    def area(self):      # 面积
        return 0
    
    def perimeter(self):    # 周长
        return 0
    

class Rectangle(Shape):     # 矩形
    def __init__(self,width,height):
        super().__init__(name='矩形')
        self.width = width      # 长
        self.height = height    # 高
        
    def area(self):
        areas = self.width * self.height
        return areas
    
    def perimeter(self):
        perimeters = 2*self.width + 2*self.height
        return perimeters
    

class Circle(Shape):    # 圆形
    def __init__(self, radius):
        super().__init__(name='圆形')
        self.radius = radius    # 半径
    
    def area(self):
        areas = 3.14 * self.radius**2
        return areas
    
    def perimeter(self):
        perimeters = 3.14 * 2 * self.radius
        return perimeters

R = Rectangle
C = Circle


def print_shape_info():
    while True:
        print('你要计算矩形的面积和周长(1),还是计算圆的面积和周长(2)')
        i = input().strip()
        if i not in ['1','2']:
            print('输入错误，请重新输入')
            continue
        else:
            if i == '1':
                w = input('输入长')
                h = input('输入高')
                try:
                    w = float(w)
                    h = float(h)
                except ValueError:
                    print('输入真确的数字')
                    continue
                s = R(w,h).area()
                c = R(w,h).perimeter()
                print(f'矩形的面积为{s},周长为{c}')
                break
            elif i == '2':
                r = input('输入半径')
                try:
                    r = float(r)
                except ValueError:
                    print('请输入正确的数字')
                    continue
                s = C(r).area()
                c = C(r).perimeter()
                print(f'圆形的面积为{s},周长为{c}')
                break
        


if __name__ == '__main__':
    print_shape_info()

# """"

"""
面向过程
"""
class Shape:    # 形状（父类）
    def __init__(self, name):
        self.name = name
        
    def area(self):      # 加上 self
        return 0
    
    def perimeter(self):
        return 0
    

class Rectangle(Shape):     # 矩形（子类）
    def __init__(self, width, height):
        super().__init__(name='矩形')  # 调用父类设置名字
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)  # 简化写法


class Circle(Shape):    # 圆形（子类）
    def __init__(self, radius):
        super().__init__(name='圆形')
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2  # 修复：加上平方
    
    def perimeter(self):
        return 3.14 * 2 * self.radius


# ✅ 核心：万能打印机（多态的体现）
# 它不关心具体是矩形还是圆，只要传进来的东西有 area() 和 perimeter() 方法就能用
def print_shape_info(shape):
    print(f'--- {shape.name} ---')
    print(f'面积为: {shape.area()}')
    print(f'周长为: {shape.perimeter()}')


# ✅ 用户交互部分（简化版）
def main():
    while True:
        choice = input('计算矩形(1)还是圆形(2)？输入q退出：').strip()
        if choice == 'q':
            break
        elif choice == '1':
            w = float(input('输入长：'))
            h = float(input('输入高：'))
            rect = Rectangle(w, h)
            print_shape_info(rect)  # 传入矩形对象，多态发生！
        elif choice == '2':
            r = float(input('输入半径：'))
            circle = Circle(r)
            print_shape_info(circle) # 传入圆形对象，多态发生！
        else:
            print('输入无效')

if __name__ == '__main__':
    main()

# ✅ 挑战：打印 MRO（方法解析顺序）
print("Rectangle 的方法查找顺序是：", Rectangle.__mro__)