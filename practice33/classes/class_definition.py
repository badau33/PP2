#1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

# Object creation / Объект құру
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

print(student1.introduce())  # Hi, I'm Alice and I'm 20 years old
print(student2.name)  # Bob
#2
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds"
    
    def get_balance(self):  # getter method
        return f"Balance: ${self.__balance}"

account = BankAccount("Alice", 1000)
print(account.deposit(500))   # Deposited $500. New balance: $1500
print(account.withdraw(200))  # Withdrew $200. New balance: $1300
# print(account.__balance)  # Error! Private attribute
print(account.get_balance())  # Balance: $1300
#3
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

circle = Circle(5)
print(f"Radius: {circle.radius}")        # Radius: 5
print(f"Area: {circle.area:.2f}")        # Area: 78.54
print(f"Circumference: {circle.circumference:.2f}")  # Circumference: 31.42

circle.radius = 7
print(f"New area: {circle.area:.2f}")    # New area: 153.94
