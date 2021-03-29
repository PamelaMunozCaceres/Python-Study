def full_name(user_info: dict) -> str:
    '''
    Join the first and last names of a specific
    user to create the full name of this user
    '''
    return user_info['name'] + user_info['last_name']