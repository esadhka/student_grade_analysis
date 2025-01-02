import pytest
from solution import calculate_average, grade_summary  # Ensure this matches the file name

# Test cases for calculate_average function
def test_calculate_average():
    # Test case 1: Typical case
    grades = [90, 85, 72, 49, 88, 91, 100, 60]
    assert calculate_average(grades) == 78.13
    
    # Test case 2: All students passed with varying grades
    grades = [50, 60, 70, 80, 90]
    assert calculate_average(grades) == 70.0
    
    # Test case 3: All students failed
    grades = [20, 30, 40]
    assert calculate_average(grades) == 30.0
    
    # Test case 4: All students with honors
    grades = [91, 95, 98, 100]
    assert calculate_average(grades) == 96.0
    
    # Test case 5: Single student case
    grades = [75]
    assert calculate_average(grades) == 75.0
    
    # Test case 6: Extreme case (mix of high and low grades)
    grades = [0, 100]
    assert calculate_average(grades) == 50.0

# Test cases for grade_summary function
def test_grade_summary():
    # Test case 1: Typical case
    grades = [90, 85, 72, 49, 88, 91, 100, 60]
    expected_output = '''Average Grade: 78.13
Number of students who passed: 6
Number of students who failed: 2
Number of students with honors: 2'''
    assert grade_summary(grades) == expected_output
    
    # Test case 2: All students passed
    grades = [50, 60, 70, 80, 90]
    expected_output = '''Average Grade: 70.0
Number of students who passed: 5
Number of students who failed: 0
Number of students with honors: 1'''
    assert grade_summary(grades) == expected_output
    
    # Test case 3: All students failed
    grades = [20, 30, 40]
    expected_output = '''Average Grade: 30.0
Number of students who passed: 0
Number of students who failed: 3
Number of students with honors: 0'''
    assert grade_summary(grades) == expected_output
    
    # Test case 4: All students with honors
    grades = [91, 95, 98, 100]
    expected_output = '''Average Grade: 96.0
Number of students who passed: 4
Number of students who failed: 0
Number of students with honors: 4'''
    assert grade_summary(grades) == expected_output
    
    # Test case 5: Mixed case with some students passing, some failing, and some with honors
    grades = [85, 45, 92, 67, 100, 48]
    expected_output = '''Average Grade: 69.5
Number of students who passed: 4
Number of students who failed: 2
Number of students with honors: 2'''
    assert grade_summary(grades) == expected_output

    # Test case 6: Single student case
    grades = [75]
    expected_output = '''Average Grade: 75.0
Number of students who passed: 1
Number of students who failed: 0
Number of students with honors: 0'''
    assert grade_summary(grades) == expected_output
    
    # Test case 7: Extreme case (mix of high and low grades)
    grades = [0, 100]
    expected_output = '''Average Grade: 50.0
Number of students who passed: 1
Number of students who failed: 1
Number of students with honors: 1'''
    assert grade_summary(grades) == expected_output
