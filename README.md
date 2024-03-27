# Student Data Analysis Script

This Python script analyzes student data to find various statistics such as highest average grade, highest and lowest grades in specific subjects, and students with grades above average in English.

## Requirements

- Python 3.12
- NumPy library

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/numpy-student-data.git
    ```

2. Navigate to the project directory:

    ```
    cd numpy-student-data
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Create an instance of the `StudentData` class by specifying the number of students and subjects:

    ```python
    num_students = 100
    subjects = ["Georgian", "Mathematics", "English", "Geography", "Physics"]
    students = StudentData(num_students, subjects)
    ```

2. Use the provided methods to retrieve various statistics:

    ```python
    # Get student with the highest average grade
    highest_avg_student, grade = students.highest_avg_score()
    print(f"Student with the highest AVG: {highest_avg_student}. Grade: {grade}")

    # Get student with the highest average grade in a specific subject
    subject = "Georgian"
    highest_avg_student, grade = students.avg_on_subject(subject)
    print(f"Student with the highest AVG in {subject}: {highest_avg_student}. Grade: {grade}")

    # Get student with the highest and lowest math grade
    highest_math_grade, lowest_math_grade = students.highest_and_lowest_math_scores()
    print(f"Student with the highest math grade: {highest_math_grade[0]}. Grade: {highest_math_grade[1]}")
    print(f"Student with the lowest math grade: {lowest_math_grade[0]}. Grade: {lowest_math_grade[1]}")

    # Get students with grades above average in English
    english_above_avg_students = students.english_above_average()
    print("Students with above average English grades:")
    for student, grade in english_above_avg_students:
        print(student, grade)
    ```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
