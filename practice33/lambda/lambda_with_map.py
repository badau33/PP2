#1
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))
print(result)
#2
number = [1, 2, 3, 4]

squares = list(map(lambda x: x ** 2, number))
print(squares)
#3
numberss = [10, 20, 30]

strings = list(map(lambda x: str(x), numberss))
print(strings)
#4
celsius = [0, 10, 20, 30]

fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(fahrenheit)

#5
a = [1, 2, 3]
b = [4, 5, 6]

sum_list = list(map(lambda x, y: x + y, a, b))
print(sum_list)
