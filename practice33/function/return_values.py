#1
def kvadrat(n):
    return n * n

natije = kvadrat(5)
print(natije)

#2
def kosu1(a, b):
    print(a + b)

def kosu2(a, b):
    return a + b

kosu1(2, 3)        # тек экранға шығарады
print(kosu2(2, 3)) # мәнді қайтарады

#3
def esep(x, y):
    return x + y, x * y

s, k = esep(3, 4)
print(s, k)

#4
def bolu(v, w):
    if w == 0:
        return "0-ге бөлуге болмайды"
    return v / w

print(bolu(10, 2))

#5
def tekser(ss):
    if ss < 0:
        return "Теріс сан"
    return "Оң сан"

print(tekser(-5))
