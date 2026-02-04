#1
for i in range(1,6):
    if i%2==0:
        continue
    print(i, end=" ")

#2
for x in range(1,11):
    if x==7:
        continue
    print(x)

#3
numbers=[3,-1,5,-2,7]
for n in numbers:
    if n<0:
        continue
    print(n, end=" ")

#4
for san in range(10,15):
    if san%2==0:
        continue
    print(san**2)

#5
words=["go","skip","run"]
for word in words:
    if word=="skip":
        continue
    print(word, end=" ")