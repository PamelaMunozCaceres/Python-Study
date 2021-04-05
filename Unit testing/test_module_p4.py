import pytest
from utils_module import \
    (function_1, compute_area_with_bug, compute_area_triangle)

class TestFunction1(object):

    def test_first_function(self):
        """
        this test should be successful
        """
        assert function_1() == 1


    def test_first_function_bad(self):
        """
        this test should fail
        """
        assert function_1(self) == 0

class TestComputeAreaWithBug(object):

    def test_compute_area_bug(self):
        """
        this test should fail if we pass a string it
        won't transform it to float
        """
        actual_value = compute_area_with_bug(2, "3")
        expected_value = 6
        msg = (f"expected value is {expected_value},"
               f" actual value is {actual_value}")
        assert actual_value == expected_value, msg

    @pytest.mark.xfail
    def test_compute_area_triangle(self):

        actual_value = compute_area_triangle(2, 3)
        expected_value = 3
        msg = (f"expected value is {expected_value},"
               f" actual value is {actual_value}")
        assert actual_value == expected_value, msg        