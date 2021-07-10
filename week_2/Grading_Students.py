def gradingStudents(grades)
    for i in grades:
        if i >= 38:
            if i % 5 > 2:
                i += 5 - (i % 5)
        print(i)


grades_count = int(input().strip())
grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)
