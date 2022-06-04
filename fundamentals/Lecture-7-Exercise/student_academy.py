def academy():

    students_count = int(input())
    student_grades = {}

    for _ in range(students_count):
        name = input()
        grade = float(input())

        if name not in student_grades:
            student_grades[name] = grade
        else:
            sum_1 = student_grades[name]
            sum_2 = sum_1 + grade
            student_grades[name] = sum_2 / 2

    for k,v in student_grades.items():
        if v >= 4.5:
            print(f"{k} -> {v:.2f}")
        
academy()