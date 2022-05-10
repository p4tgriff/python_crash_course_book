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

family_members = {
    'patrickg': {
        'first_name': 'Patrick',
        'last_name': 'Griffith',
        'age': 33,
        'city': 'Fort Worth'
    },

    'brittnig': {
        'first_name': 'Brittni',
        'last_name': 'Griffith',
        'age': 31,
        'city': 'Argyle'
    },

    'richardg': {
        'first_name': 'Rick',
        'last_name': 'Griffith',
        'age': 67,
        'city': 'Fort Worth'
    },

    'debbieg': {
        'first_name': 'Debbie',
        'last_name': 'Griffith',
        'age': 66,
        'city': 'Saginaw'
    },
}

for persons, people in family_members.items():
    print(
        f"My name is {people['first_name']} and I am {people['age']} years old.")
    print(f"I live in {people['city']}.")
