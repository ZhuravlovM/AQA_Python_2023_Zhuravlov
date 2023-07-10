student_marks = {"Vasily": 5, "Sergiy": 3, "Oksana": 4, "Mark": 2, "Katya": 4}

def higher_average_mark(marks):
    average = sum(marks.values()) / len(marks)

    student_higher_marks = []
    for student, mark in marks.items():
        if mark > average:
            student_higher_marks.append(student)

    return average, student_higher_marks


average_mark, check_marks = higher_average_mark(student_marks)
print("Середній бал у групі студентів:", average_mark)
print("Студенти, у яких бал вищий середнього:", check_marks)
