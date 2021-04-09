import pytest
import os
from src.readmodule.read import read_count


@pytest.fixture
def setup_data():
    path = 'file.txt'
    character = 'a'
    with open(path, 'w') as f:
        f.write("Hello my name is Pamela")
    yield path, character
    os.remove(path)
    os.remove(f"character {character}.txt")
    

    
class TestReading(object):
    
    def test_read(self, setup_data):
        path, character = setup_data
        # Call the function
        read_count(path, character)
        # Check the result
        with open(f"character {character}.txt", 'r') as f:
            number = f.read()
        assert int(float(number)) == 3, f'value is {int(number)}'