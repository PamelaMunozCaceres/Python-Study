import pytest
from utils_module import \
    (function_1, compute_area_with_bug, compute_area)


def test_first_function():
    """
    this test should be successful
    """
    assert function_1() == 1

    
def test_first_function_bad():
    """
    this test should fail
    """
    assert function_1() == 0
    
    
def test_compute_area_bug():
    """
    this test should fail if we pass a string it
    won't transform it to float
    """
    actual_value = compute_area_with_bug(2, "3")
    expected_value = 6
    msg = (f"expected value is {expected_value},"
           f" actual value is {actual_value}")
    assert actual_value == expected_value, msg

    
def test_compute_area():
    """
    this test should be successful
    """
    actual_value = compute_area(2, "3")
    expected_value = 6
    msg = (f"expected value is {expected_value},"
           f" actual value is {actual_value}")
    assert isinstance(actual_value, float)
    assert actual_value == expected_value, msg