user_names = ['admin', 'Patrick', 'Brittni', 'Jon', 'Allie']

for user_name in user_names:
    if user_name == 'admin':
        print(
            f"Hello {user_name}, would you like to see a status report?")
    else:
        print(f"Hello {user_name}, welcome back!")


# This is not correct.  Need to figure out why it's not posting an error about matching.

current_users = ['Patrick', 'Brittni', 'Jon', 'Allie', 'Ryan']

new_users = ['Liam', 'Lucas', 'Nate', 'Allie', 'Ryan']

for new_user in new_users:
    if new_user == current_users:
        print(f'This user already exists: {new_user}')
    else:
        print('New user created!')
