#1
numbers = [5, 2, 8, 1, 9, 3]
sorted_numbers = sorted(numbers, key=lambda x: x)
print("Sorted numbers:", sorted_numbers)  # [1, 2, 3, 5, 8, 9]

# Reverse order / Кері ретпен
reverse_sorted = sorted(numbers, key=lambda x: x, reverse=True)
print("Reverse sorted:", reverse_sorted)  # [9, 8, 5, 3, 2, 1]
#2
words = ["python", "java", "c", "javascript", "go", "rust"]
by_length = sorted(words, key=lambda x: len(x))
print("By length:", by_length)  # ['c', 'go', 'java', 'rust', 'python', 'javascript']

by_length_desc = sorted(words, key=lambda x: len(x), reverse=True)
print("By length desc:", by_length_desc)  # ['javascript', 'python', 'rust', 'java', 'go', 'c']
#3
cities = ["Almaty", "Astana", "Shymkent", "Aktau", "Karagandy"]
by_last_letter = sorted(cities, key=lambda x: x[-1])
print("By last letter:", by_last_letter)  # ['Astana', 'Almaty', 'Karagandy', 'Shymkent', 'Aktau']
#4
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "David", "grade": 88}
]

by_grade = sorted(students, key=lambda x: x["grade"])
print("By grade (ascending):")
for s in by_grade:
    print(f"{s['name']}: {s['grade']}")
# Charlie: 78
# Alice: 85  
# David: 88
# Bob: 92

by_grade_desc = sorted(students, key=lambda x: x["grade"], reverse=True)
print("\nBy grade (descending):")
for s in by_grade_desc:
    print(f"{s['name']}: {s['grade']}")

#5
people = [
    {"name": "John", "age": 25},
    {"name": "Emma", "age": 22},
    {"name": "Tom", "age": 30},
    {"name": "Lisa", "age": 19}
]

by_age = sorted(people, key=lambda x: x["age"])
for person in by_age:
    print(f"{person['name']} - {person['age']} years")
# Lisa - 19 years
# Emma - 22 years  
# John - 25 years
# Tom - 30 years