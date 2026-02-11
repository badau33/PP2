#1
class Animal:
    def sound(self):
        return "Some sound"
    
    def move(self):
        return "Some movement"

class Dog(Animal):
    def sound(self):  # Override parent method
        return "Woof!"
    
    def move(self):   # Override parent method
        return "Run"

dog = Dog()
print(dog.sound())  # Woof!
print(dog.move())   # Run
#2
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        parent_greeting = super().greet()  # Call parent method
        return f"{parent_greeting} and Hello from Child"

child = Child()
print(child.greet())  # Hello from Parent and Hello from Child
#3
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created: {self.name}")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)  # Call parent constructor
        self.student_id = student_id
        print(f"Student created: {self.student_id}")

student = Student("Aibek", "S001")
# Person created: Aibek
# Student created: S001
#4
class Calculator:
    def calculate(self, a, b):
        return a + b

class AdvancedCalculator(Calculator):
    def calculate(self, a, b, operation="add"):  # Override with extra parameter
        if operation == "add":
            return super().calculate(a, b)
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b if b != 0 else "Error"

calc = AdvancedCalculator()
print(calc.calculate(10, 5))          # 15 (add)
print(calc.calculate(10, 5, "multiply"))  # 50
print(calc.calculate(10, 5, "divide"))    # 2.0