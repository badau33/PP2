#1
class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent __init__: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent __init__
        self.age = age
        print(f"Child __init__: {self.age}")

child = Child("Aibek", 20)
# Parent __init__: Aibek
# Child __init__: 20'
#2
class Animal:
    def speak(self):
        return "Animal sound"
    
    def move(self):
        return "Animal moves"

class Dog(Animal):
    def speak(self):
        parent_sound = super().speak()  # Call parent method
        return f"{parent_sound} -> Woof!"
    
    def move(self):
        return super().move() + " -> runs"

dog = Dog()
print(dog.speak())  # Animal sound -> Woof!
print(dog.move())   # Animal moves -> runs
#3
class GrandParent:
    def __init__(self):
        print("GrandParent __init__")
        self.family = "Smith"

class Parent(GrandParent):
    def __init__(self):
        super().__init__()
        print("Parent __init__")
        self.house = "Big House"

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child __init__")
        self.toy = "Car"

child = Child()
# GrandParent __init__
# Parent __init__
# Child __init__
print(child.family)  # Smith
print(child.house)   # Big House
print(child.toy)     # Car
#4
class A:
    def __init__(self):
        print("A __init__")
        self.a = "A value"

class B:
    def __init__(self):
        print("B __init__")
        self.b = "B value"

class C(A, B):
    def __init__(self):
        super().__init__()  # Calls A.__init__ (MRO order)
        print("C __init__")
        self.c = "C value"

c = C()
print(c.a)  # A value
# print(c.b)  # Error! B.__init__ not called
print(C.__mro__)  # (<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>)