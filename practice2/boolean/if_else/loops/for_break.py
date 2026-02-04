#1
for i in range(1,6):
    if  i==5:
        break
    print(i)
#2
num=[3,7,8,2,4]
for n in num:
    if n==8:
        break
    print(n)
#3
sandar=[1,3,5,11,16,9]
for even in sandar:
    if even%2==0:
        print("Found even:", even)
        break
#4
nums=[4,77,-22,57,-11]
for d in nums:
    if d<0:
        print("First negative:", d)
        break
#5
sann=[1,2,3,4,5,6,7,8,9]
for s in reversed(sann):
    if sann==7:
        break
    print(sann)