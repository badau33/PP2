#1
kvadrat = lambda x: x * x
print(kvadrat(6))

#2
kosu = lambda a, b: a + b
print(kosu(3, 7))

#3
zhuptpa = lambda n: "Жұп" if n % 2 == 0 else "Тақ"
print(zhuptpa(10))

#4
sandar = [1, 2, 3, 4]
kv = list(map(lambda x: x * 2, sandar))
print(kv)

#5
sandr = [1, 2, 3, 4, 5, 6]
zhup = list(filter(lambda x: x % 2 == 0, sandr))
print(zhup)
