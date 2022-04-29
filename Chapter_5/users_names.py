user_names = ['admin', 'Patrick', 'Brittni', 'Jon', 'Allie']

for user_name in user_names:
    if user_name == 'admin':
        print(
            f"Hello {user_name}, would you like to see a status report?")
    else:
        print(f"Hello {user_name}, welcome back!")
