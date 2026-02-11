#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)  # [2, 4, 6, 8, 10]
#2
number = [-5, 3, -1, 7, -2, 0, 8, -4]
positive = list(filter(lambda x: x > 0, number))
print("Positive numbers:", positive)  # [3, 7, 8]
#3
words = ["madam", "hello", "racecar", "python", "level", "world"]
palindromes = list(filter(lambda x: x == x[::-1], words))
print("Palindromes:", palindromes)  # ['madam', 'racecar', 'level']
#4
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "C"},
    {"name": "Charlie", "grade": "A"},
    {"name": "David", "grade": "B"}
]

a_students = list(filter(lambda x: x["grade"] == "A", students))
for student in a_students:
    print(f"{student['name']} - {student['grade']}")
# Alice - A
# Charlie - A
#5
strings = ["hello", "", "world", " ", "python", "", "code"]
non_empty = list(filter(lambda x: x.strip() != "", strings))
print("Non-empty strings:", non_empty)  # ['hello', 'world', ' ', 'python', 'code']