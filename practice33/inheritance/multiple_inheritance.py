#1
class Father:
    def __init__(self, father_name):
        self.father_name = father_name
    
    def father_info(self):
        return f"Father: {self.father_name}"

class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name
    
    def mother_info(self):
        return f"Mother: {self.mother_name}"

class Child(Father, Mother):  # Inherit from both
    def __init__(self, name, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.name = name
    
    def child_info(self):
        return f"Child: {self.name}"

child = Child("Aibek", "Askar", "Aigerim")
print(child.father_info())  # Father: Askar
print(child.mother_info())  # Mother: Aigerim
print(child.child_info())   # Child: Aibek
#2
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
        B.__init__(self)    # Manually call B.__init__
        print("C __init__")
        self.c = "C value"

c = C()
# A __init__
# B __init__
# C __init__
print(c.a)  # A value
print(c.b)  # B value
print(c.c)  # C value
#3
class X:
    def process(self):
        return "X"

class Y:
    def process(self):
        return "Y"

class Z(X, Y):
    pass

class W(Y, X):
    pass

z = Z()
w = W()
print(z.process())  # X (follows MRO: Z -> X -> Y)
print(w.process())  # Y (follows MRO: W -> Y -> X)

print(Z.__mro__)  # (<class 'Z'>, <class 'X'>, <class 'Y'>, <class 'object'>)
print(W.__mro__)  # (<class 'W'>, <class 'Y'>, <class 'X'>, <class 'object'>)