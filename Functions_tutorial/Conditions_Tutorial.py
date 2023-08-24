def get_grade(score):
    grade = "F"
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'

    return grade


print(get_grade(80))
