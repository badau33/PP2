#1
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i, end=" ")

#2
nums = [2, -3, 5, -1, 7]
i = 0
while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue
    print(nums[i] )
    i += 1

#3
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i, end= " ")

#4
i = 5
while i > 0:
    if i == 3:
        i -= 1
        continue
    print(i)
    i -= 1

#5
i = 0
while i < 5:
    num = int(input("Сан енгізіңіз: "))
    i += 1
    if num == 0:
        continue
    print("Сіз енгіздіңіз:", num, end=" ")
