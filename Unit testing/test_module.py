import pytest
from utils_module import function_1

def test_first_function():
    assert function_1() == 1
    
def test_first_function_bad():
    assert function_1() == 0