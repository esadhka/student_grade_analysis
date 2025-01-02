from typing import List

def calculate_average(grades: List[int]) -> float:
    """
    This function calculates the average grade from the list of grades.
    The average should be rounded to two decimal places.
    """
    return round(sum(grades) / len(grades), 2)

def grade_summary(grades: List[int]) -> str:
    """
    This function generates a summary of the students' grades:
    - Average grade (rounded to two decimal places)
    - Number of students who passed (grade >= 50)
    - Number of students who failed (grade < 50)
    - Number of students with honors (grade >= 90)
    """
    average = calculate_average(grades)
    passed = sum(1 for grade in grades if grade >= 50)
    failed = sum(1 for grade in grades if grade < 50)
    honors = sum(1 for grade in grades if grade >= 90)
    
    return f"""Average Grade: {average}
Number of students who passed: {passed}
Number of students who failed: {failed}
Number of students with honors: {honors}
"""
