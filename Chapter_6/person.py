patrick = {
    'first_name': 'Patrick',
    'last_name': 'Griffith',
    'age': 33,
    'city': 'Fort Worth'
}

print(patrick)

patrick_name = patrick.get(
    'first_name', 'couldnt get first name.')
print(patrick_name)
