class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f'我叫{self.name},今年{self.age}岁了')

class Student(Person):
    def __init__(self, name, age,student_id,**kwarges):
        super().__init__(name, age,**kwarges)
        self.student = student_id
    
    def introduce(self):
        super().introduce()
        print(f'我的学号是{self.student}')

class Teacher(Person):
    def __init__(self, name, age,subject,**kwarges):
        super().__init__(name, age,**kwarges)
        self.subject = subject
    
    def introduce(self):
        super().introduce()
        print(f'我教的科目是{self.subject}')


class TeachingAssistant(Student,Teacher):
    pass

T = TeachingAssistant('张振伟',age=18,student_id='5201314',subject="python")
T.introduce()  

print("\nMRO 顺序",TeachingAssistant.__mro__)
