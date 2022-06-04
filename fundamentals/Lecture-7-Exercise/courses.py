def courses():
    
    courses = {}

    while True:
        input_line = input()
        if input_line == 'end':
            break

        course_name, student_name = input_line.split(' : ')
        if course_name not in courses:
            courses[course_name] = []
        courses[course_name].append(student_name)

    for course_name in courses.keys():
        students = courses.get(course_name)
        registered_students = len(students)
        print (f"{course_name}: {registered_students}")
        formated_students = [f"-- {name}" for name in students]
        print(*formated_students, sep='\n')
        
courses()