def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def print_student_grades(student_data):
    for name, score in student_data.items():
        grade = calculate_grade(score)
        print(f"{name}: Score = {score}, Grade = {grade}")
