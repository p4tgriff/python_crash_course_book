def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'albert', 'einstein', location='princeton', field='physics')
print(user_profile)


my_profile = build_profile('Patrick', 'Griffith',
                           location='Texas', married='yes', children='yes')
print(my_profile)
