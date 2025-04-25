import math

number_of_students = int(input())
lectures = int(input())
additional_bonus = int(input())
max_bonus_points = 0
student_attendances = 0

for student in range(1, number_of_students + 1):
    attendance_fro_courses_of_each_student = int(input())
    total_bonus = attendance_fro_courses_of_each_student / lectures * (5 + additional_bonus)
    if total_bonus > max_bonus_points:
        max_bonus_points = total_bonus
        student_attendances = attendance_fro_courses_of_each_student
    elif total_bonus < max_bonus_points:
        continue


print(f'Max Bonus: {math.ceil(max_bonus_points)}.')
print(f'The student has attended {student_attendances} lectures.')
