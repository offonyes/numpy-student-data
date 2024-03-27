from students import StudentData

# Create a class
num_students = 100
subjects = ["Georgian", "Mathematics", "English", "Geography", "Physics"]
students = StudentData(num_students, subjects)

# Get student with the highest average grade
highest_avg_student, grade = students.highest_avg_score()
print(f"Student with the highest AVG:{highest_avg_student}. Grade: {grade}")

# Get student with the highest average grade on specific subject
subject = "Georgian"
highest_avg_student, grade = students.avg_on_subject(subject)
print(f"Student with the highest AVG in {subject}: {highest_avg_student}. Grade: {grade}")

# Get student with highest and lowest math grade
highest_math_grade, lowest_math_grade = students.highest_and_lowest_math_scores()
print(f"Student with the highest math grade: {highest_math_grade[0]}. Grade: {highest_math_grade[1]}")
print(f"Student with the lowest math grade: {lowest_math_grade[0]}. Grade: {lowest_math_grade[1]}")

# Get students grades above average
english_above_avg_students = students.english_above_average()
print("Students with above average English grades:")
for student, grade in english_above_avg_students:
    print(student, grade)
