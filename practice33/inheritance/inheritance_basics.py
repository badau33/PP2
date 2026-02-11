#1
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        return f"{self.name} says Woof!"

class Cat(Animal):  # Cat inherits from Animal
    def meow(self):
        return f"{self.name} says Meow!"

dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.eat())    # Rex is eating (inherited)
print(dog.bark())   # Rex says Woof! (own method)
print(cat.sleep())  # Whiskers is sleeping (inherited)
print(cat.meow())   # Whiskers says Meow! (own method)
#2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
    
    def introduce(self):
        return f"{super().introduce()} - Student ID: {self.student_id}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def introduce(self):
        return f"{super().introduce()} - Teaches {self.subject}"

student = Student("Aibek", 20, "S001")
teacher = Teacher("Aigerim", 35, "Math")

print(student.introduce())  # Hi, I'm Aibek, 20 years old - Student ID: S001
print(teacher.introduce())  # Hi, I'm Aigerim, 35 years old - Teaches Math
#3
class Flyable:
    def fly(self):
        return "Flying in the sky"

class Swimmable:
    def swim(self):
        return "Swimming in water"

class Duck(Flyable, Swimmable):  # Inherit from two classes
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        return f"{self.name} says Quack!"

duck = Duck("Donald")
print(duck.fly())   # Flying in the sky (from Flyable)
print(duck.swim())  # Swimming in water (from Swimmable)
print(duck.quack()) # Donald says Quack! (own method)
#4
# 7. Method Order Resolution (MRO) / Методтарды іздеу реті
class A:
    def process(self):
        return "A"

class B(A):
    def process(self):
        return "B"

class C(A):
    def process(self):
        return "C"

class D(B, C):  # Multiple inheritance
    pass

d = D()
print(d.process())  # B (follows MRO: D -> B -> C -> A)
print(D.__mro__)    # Shows method resolution order