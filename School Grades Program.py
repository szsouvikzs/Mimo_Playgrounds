# Use python to process some information about a student's grades to create a report

student_name = "Sam"
math_grade = 88
science_grade = 75
english_grade = 90
geology_grade = 69
total_grade = math_grade+science_grade+english_grade+geology_grade
max_grade = 400
total_percentage = total_grade/max_grade*100
print(f"Sam's total percentage is {total_percentage}%")
total_percentage = int(total_percentage)
did_student_pass = total_percentage >= 50
sporting_activities = bool(0)
print(f"Sam participated in sporting activities: {sporting_activities}")
print(f"Sam's total percentage as an integer is {total_percentage}%")
print(f"Sam passed to the next semester: {did_student_pass}")
