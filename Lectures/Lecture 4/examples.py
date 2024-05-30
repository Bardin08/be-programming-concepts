gradebook = {
    "John": {
        "Math": [75, 35, 45, 60],
        "Economics": [20, 30, 40, 50],
        "History": [80, 90, 100, 95]
    },
    "Tom": {
        "Math": [30, 40, 50, 60],
        "Economics": [80, 90, 100, 95],
        "History": [90, 80, 70, 60]
    },
    "Jessica": {
        "Math": [90, 80, 70, 60],
        "Economics": [20, 30, 40, 50],
        "History": [30, 40, 50, 60]
    },
}

tom_math_grades = gradebook["Tom"]["Math"]
print(tom_math_grades)

tom_grades = gradebook["Tom"]
print(tom_grades)

tom_math_grades = tom_grades["Math"]
print(tom_math_grades)


for student, subjects in gradebook.items():
    print(f"Student: {student}")
    for subject, scores in subjects.items():
        print(f"Subject: {subject}")
        print(f"Scores: {scores}")
        print(f"Average: {sum(scores) / len(scores)}")
    print()

print(gradebook['Jessica']['Math'])

student_names = list(gradebook.keys())
marks = []
for subjects in gradebook.values():
    for scores in subjects.values():
        marks.extend(scores)


gradebook.pop("Tom")
del gradebook["Jessica"]

print(gradebook)

squares_dict = {}
for i in range(1, 11):
    squares_dict[i] = i ** 2

print(squares_dict)

squares_dict_v2 = {i: i ** 2 for i in range(1, 11)}

















