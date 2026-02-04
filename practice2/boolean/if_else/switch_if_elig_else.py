#1
san=int(input())
if san%2==0:
    print("even")
else:
    print("odd")
#2
point=85
if point>=90:
    print("A")
elif point>=75:
    print("B")
elif point>=60:
    print("C")
else:
    print("F")
#3
num=int(input())
if num>0:
    print("positive")
elif num==0:
    print("zero")
else:
    print("negative")
#4
x=int(input())
y=int(input())
if x>y:
    print("X үлкен")
elif x<y:
    print("Y үлкен")
else:
    print("X пен Y тең")

#5
birsan=int(input())
if birsan%3==0 and birsan%5==0:
    print("FizzBuzz")
elif birsan%3==0:
    print("Fizz")
elif birsan%5==0:
    print("Buzz")
else:
    print(birsan)