#1
def summa(*args):
    return sum(args)

print(summa(1, 2, 3))
print(summa(5, 10, 15, 20))

#2
def korset(*arg):
    for san in arg:
        print(san)

korset(4, 7, 9)

#3
def akparat(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

akparat(at="Али", zhas=16, qala="Астана")

#4
def barligi(*ar, **kwar):
    print("Args:", ar)
    print("Kwargs:", kwar)

barligi(1, 2, 3, at="Нұр", zhas=17)

#5
def mysal(a, b, *argss, **kwargss):
    print(a, b)
