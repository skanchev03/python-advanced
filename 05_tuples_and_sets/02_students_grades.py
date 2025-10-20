n = int(input())
students = {}
student_set = set()

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)

    if name not in students:
        students[name] = []
    students[name].append(grade)
    student_set.add(name)

for name in student_set:
    grades = students[name]
    print(f"{name} -> {' '.join(f'{x:.2f}' for x in grades)} (avg: {sum(grades) / len(grades):.2f})")
