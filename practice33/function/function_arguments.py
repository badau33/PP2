#1
def kosu(a, b):
    return a + b

print(kosu(4, 6))

#2
def tanystyr(at, zhas):
    print(at, zhas, "жаста")

tanystyr(zhas=17, at="Айбек")

#3
def summa(*args):
    return sum(args)

print(summa(1, 2, 3, 4))

#4
def akparat(**kwargs):
    for k, v in kwargs.items():
        print(k, ":", v)

akparat(at="Нұр", zhas=16, qala="Алматы")

#5
def salem(esim="Дос"):
    print("Сәлем,", esim)

salem()
salem("Аружан")