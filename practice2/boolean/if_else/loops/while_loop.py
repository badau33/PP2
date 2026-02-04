#1
i=1
while i<=5:
    print(i)
    i+=1
#2
i=1
sum=0
while i<=10:
    sum+=i
    i+=1
print(sum)
#3
i=5
while i>0:
    print(i)
    i-=1
#4
a,b=0,1
n=int(input())
count=0
while count<n:
    print(a,end= " ")
    a,b=b,a+b
    count+=1
#5
answer= ""
while answer.lower()!= "иә":
    answer=input("Сіз дайынсыз ба ? (иә/жоқ)")

print("Тамаша, Бастаймыз!")