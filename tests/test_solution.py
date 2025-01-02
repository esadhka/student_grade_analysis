import pytest
from assignment.solution import sum_of_evens

# Test example cases
def test_example_cases():
    # Test with mixed positive and negative numbers
    assert sum_of_evens([1, 2, 3, 4, 5]) == 6
    assert sum_of_evens([1, 3, 5, 7]) == 0
    assert sum_of_evens([]) == 0

# Test with negative numbers
def test_negative_numbers():
    assert sum_of_evens([-2, -4, -6]) == -12
    assert sum_of_evens([-1, -3, -5]) == 0

# Test with large numbers in range
def test_large_numbers():
    assert sum_of_evens([1000, 1001, 2000]) == 3000
    assert sum_of_evens([999, 1001, 1003]) == 0

# Test with a list that contains only one number
def test_edge_cases():
    assert sum_of_evens([2]) == 2
    assert sum_of_evens([1]) == 0
    assert sum_of_evens([0, 1, 2, 3, 4, 5]) == 6
