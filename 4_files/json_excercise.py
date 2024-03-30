"""This exercise tests your understanding of working with json files."""

from typing import TypedDict
import json

StudentStatistics = TypedDict(
    'StudentStatistics',
    {
        'student_code': str,
        'exercise_id': str,
        'submission_count': int,
        'best_grade': float,
    },
)

ExerciseStatistics = TypedDict(
    'ExerciseStatistics',
    {
        'exercise_id': str,
        'amount_of_students_attempted': int,
        'amount_of_students_completed': int,
        'average_submission_grade': float,
    },
)

# Write your code here


def add_submission(student_code: str, exercise_id: str, submittedAt: str, grade: float):
    """Add submission to json file."""
    if grade < 0 or grade > 5:
        return False
    with open('student_submissions.json', 'r') as json_file:
        json_dictionary = json.load(json_file)
        json_file.close()
        print(json_dictionary)
        for index, student in enumerate(json_dictionary['students']):
            if student_code in student['studentCode']:
                json_dictionary['students'][index]["submissions"].append({
                    "exerciseId": exercise_id,
                    "submittedAt": submittedAt,
                    "grade": grade
                })
                with open('student_submissions.json', 'w') as json_file_write:
                    json.dump(json_dictionary, json_file_write)
                return True
        return False


def get_student_statistics(student_code: str, exercise_id: str):
    """Find student statistics from json file."""
    count_submission = 0
    best_grade = 0.0

    with open('student_submissions.json', 'r') as json_file:
        json_data = json.load(json_file)

    for student in json_data.get('students', []):
        if student_code == student.get('studentCode', ''):
            submissions = student.get('submissions', [])
            if submissions:
                count_submission = len(submissions) - 1
                best_grade = max(submission['grade'] for submission in submissions)
            return StudentStatistics(
                student_code=student_code,
                exercise_id=exercise_id,
                submission_count=count_submission,
                best_grade=best_grade
            )

    return None


def get_exercise_statistics(exercise_id: str) -> ExerciseStatistics:
    """Get exercise statistics from the id."""
    students_attempted = set()
    students_completed = set()
    grades = 0
    total_exercises = 0

    with open('student_submissions.json', 'r') as json_file:
        json_data = json.load(json_file)

    for student in json_data.get('students', []):
        has_submission = False
        for exercise in student.get('submissions', []):
            if exercise_id == exercise['exerciseId']:
                students_attempted.add(student['studentCode'])
                has_submission = True

                if exercise['grade'] == 5.0:
                    students_completed.add(student['studentCode'])

                grades += exercise['grade']
                total_exercises += 1

        if not has_submission:
            students_attempted.discard(student['studentCode'])

    average_grade = round(grades / total_exercises, 2) if total_exercises > 0 else 0.0

    return ExerciseStatistics(
        exercise_id=exercise_id,
        amount_of_students_attempted=len(students_attempted),
        amount_of_students_completed=len(students_completed),
        average_submission_grade=average_grade
    )
