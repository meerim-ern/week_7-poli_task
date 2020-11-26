# import math

# class Shape:
#     def area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height
#     def area(self):
#         Shape.area(self)
#         self.s = (self.base * self.height)/2
#         print("The area of triangle",self.s)

# class Square(Shape):
#     def __init__(self,length):
#         self.length = length

#     def area(self):
#         super().area()
#         self.s = (self.length**2)
#         print("The area of square",self.s)

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
    
#     def area(self):
#         super().area()
#         self.s =math.pi * self.radius
#         print("The area of circle",self.s)

# obj =[
#     Triangle(4,5),
#     Square(5),
#     Circle(5)
# ]

# def get_shape_area():
#     for x in obj:
#         x.area()
# get_shape_area()

##2

# class Person:
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname = surname

#     def get_info(self):        
#         print("Привет, меня зовут ",self.name, self.surname)

# class Employee(Person):
#     def __init__(self,name,surname,company,position):
#         super().__init__(name,surname)
#         self.company = company
#         self.position = position
#     def get_info(self):
#         print("Привет, меня зовут ", self.name, self.surname,"я работаю в ", self.company, ", должность: ", self.position)

# class Student(Person):
#     def __init__(self,name,surname,university,course):
#         super().__init__(name,surname)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         print("Привет, меня зовут ",self.name, self.surname,", я учусь в ", self.university,", специализация:", self.course)

# obj = [
#     Person("Иван", "Иванович"),
#     Employee("Иван", "Иванович","Газпром","бухгалтер"),
#     Student("Иван", "Иванович","МГУ","MBA")
# ]

# def get_human_info():
#     for person in obj:
#         person.get_info()
# get_human_info()

##3


class  MyInt(int):
    def add(self,num1,num2):
        self.num1 = int(num1)
        self.num2 = int(num2)
        print("Это сложение: число1 + число2. Cумма равна: ", self.num1 + self.num2)

class MyStr(str):
    def add(self,num1,num2):
        self.num1 = str(num1)
        self.num2 = str(num2)
        print("Это конкатенация: число1 + число2. Результат: ", self.num1 + self.num2)

obj = MyInt()
obj1 = MyStr()
    
def add_objects(num1,num2):    
    obj.add(num1,num2)
    obj1.add(num1,num2)
   
add_objects(1,2)
add_objects("2","2")
        
        
       






