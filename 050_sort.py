# sort() method used with lists
# sorted() function used with iterables

# -----------------------------------------------------
students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]

students.sort(reverse=True)

for i in students:
    print(i)

# -----------------------------------------------------
students_tuple = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")
sorted_students_tuple = sorted(students_tuple, reverse=True)

for i in sorted_students_tuple:
    print(i)

# -----------------------------------------------------
students_2 = [
    ("Squidward", "F", 60),
    ("Sandy", "A", 33),
    ("Patric", "D", 36),
    ("Spongebob", "B", 20),
    ("Mr. Krabs", "C", 78),
]
students_2.sort()

for i in students_2:
    print(i)

grade = lambda grades: grades[1]  # grade is the value with index 1
students_2.sort(key=grade, reverse=True)  # sorting by the grades

for i in students_2:
    print(i)

age = lambda ages: ages[2]
students_2.sort(key=age)

for i in students_2:
    print(i)
