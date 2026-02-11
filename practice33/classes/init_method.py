#1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Aibek", 25)
print(person.name)  # Aibek
print(person.age)   # 25
#2
class Student:
    def __init__(self, name="Unknown", grade=0):
        self.name = name
        self.grade = grade

s1 = Student("Aigerim", 90)
s2 = Student()  # default values

print(s1.name, s1.grade)  # Aigerim 90
print(s2.name, s2.grade)  # Unknown 0
#3
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height
        self.perimeter = 2 * (width + height)

rect = Rectangle(5, 3)
print(f"Area: {rect.area}")        # Area: 15
print(f"Perimeter: {rect.perimeter}")  # Perimeter: 16
#4
class Phone:
    def __init__(self, brand, model, specs):
        self.brand = brand
        self.model = model
        self.specs = specs

iphone = Phone("Apple", "iPhone 13", {"ram": "4GB", "storage": "128GB"})
print(iphone.specs["storage"])  # 128GB