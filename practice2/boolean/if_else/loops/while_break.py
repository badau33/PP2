#1
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1
#2
while True:
    word = input("Сөз енгізіңіз (тоқтату үшін 'stop'): ")
    if word.lower() == "stop":
        break
    print("Сіз енгіздіңіз:", word)
#3
i = 1
while True:
    if i % 2 != 0:
        break
    print(i)
    i += 2
#4
import random

while True:
    num = random.randint(1, 10)
    print(num)
    if num == 7:
        print("Сан 7 шықты! Тоқтату.")
        break
#5
while True:
    number = int(input("Сан енгізіңіз (тоқтату үшін 0): "))
    if number == 0:
        break
    print("Сіз енгіздіңіз:", number)

