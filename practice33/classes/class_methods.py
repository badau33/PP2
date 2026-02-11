#1
class Student:
    school = "№1 High School"
    
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
    
    def __init__(self, name):
        self.name = name

print(Student.school)  # №1 High School
Student.change_school("№5 Gymnasium")
print(Student.school)  # №5 Gymnasium
#2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2026 - birth_year  # current year 2026
        return cls(name, age)

person1 = Person("Aibek", 25)
person2 = Person.from_birth_year("Aigerim", 2000)

print(person1.name, person1.age)  # Aibek 25
print(person2.name, person2.age)  # Aigerim 26
#3
class Employee:
    company = "TechCorp"
    count = 0
    
    def __init__(self, name):
        self.name = name
        Employee.count += 1
    
    @classmethod
    def get_count(cls):
        return f"Total employees: {cls.count}"
    
    @classmethod
    def set_company(cls, new_company):
        cls.company = new_company

emp1 = Employee("John")
emp2 = Employee("Emma")
emp3 = Employee("Bob")

print(Employee.get_count())  # Total employees: 3
Employee.set_company("CodeLab")
print(emp1.company)  # CodeLab
#4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height
    
    @classmethod
    def square(cls, side):
        return cls(side, side)
    
    @classmethod
    def from_string(cls, text):
        w, h = map(int, text.split(','))
        return cls(w, h)

rect1 = Rectangle(5, 3)
rect2 = Rectangle.square(4)
rect3 = Rectangle.from_string("6,2")

print(rect1.area)  # 15
print(rect2.area)  # 16
print(rect3.area)  # 12