#1
class Student:
    school = "High School #1"  # class variable
    year = 2026               # class variable
    
    def __init__(self, name):
        self.name = name      # instance variable

s1 = Student("Aibek")
s2 = Student("Aigerim")

print(s1.school)  # High School #1
print(s2.school)  # High School #1
print(Student.school)  # High School #1
#2
class Employee:
    total_employees = 0  # class variable
    
    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1
    
    def __del__(self):
        Employee.total_employees -= 1

e1 = Employee("John")
e2 = Employee("Emma")
e3 = Employee("Bob")

print(Employee.total_employees)  # 3
del e2
print(Employee.total_employees)  # 2
#3
class Database:
    host = "localhost"
    port = 5432
    username = "admin"
    password = "12345"
    
    def __init__(self, name):
        self.name = name
    
    def connection_string(self):
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.name}"

db1 = Database("mydb")
db2 = Database("testdb")

print(db1.connection_string())  # postgresql://admin:12345@localhost:5432/mydb
print(db2.connection_string())  # postgresql://admin:12345@localhost:5432/testdb

Database.host = "192.168.1.100"
print(db1.connection_string())  # postgresql://admin:12345@192.168.1.100:5432/mydb
#4
# 6. Constants / Тұрақтылар
class MathConstants:
    PI = 3.14159
    E = 2.71828
    GOLDEN_RATIO = 1.61803
    
    @classmethod
    def circle_area(cls, radius):
        return cls.PI * radius ** 2

print(MathConstants.PI)  # 3.14159
print(MathConstants.circle_area(5))  # 78.53975