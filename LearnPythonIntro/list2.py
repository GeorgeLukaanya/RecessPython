def get_student_data():
    student_data = {}
    n = int(input("How many students? "))

    for _ in range(n):
        name = input("Enter student name: ")
        score = int(input(f"Enter score for {name}: "))
        student_data[name] = score

    return student_data

get_student_data()