import pytest
from utils_module_p2 import full_name


def test_full_name_without_key():
    '''
    We want our full user name to have a first
    and last name, so if it does not have it,
    we expect the function to fail.
    The test will succeed if the function
    actually fails
    '''
    user = {'last_name': 'Munoz'}
    with pytest.raises(KeyError) as exception_info:
        full_name(user)
    assert exception_info.match('name')
        

def test_full_name_with_list():
    '''
    we want our full name to be a string and not
    a list, so if it ends up being a list,
    we expect the function to fail.
    The test will succeed if the function
    actually fails
    '''
    user = {'last_name': ['Munoz'], 'name': ['Pamela']}
    with pytest.raises(TypeError):
        full_name(user)