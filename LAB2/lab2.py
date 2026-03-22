n = int(input())
numbers=[]
for i in range(n):
    num=input()
    numbers.append(num)

count=0

for unique in set(numbers):
    if numbers.count(unique)==3:
        count+=1

print(count)
