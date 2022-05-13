# pets = ['dog_0', 'dog_1', 'dog_2', 'cat']

dog_0 = {
    'name': 'Lucky',
    'owner': 'Tim',
    'age': '3'
}

dog_1 = {
    'name': 'Jolie',
    'owner': 'Sara',
    'age': '8'
}

dog_2 = {
    'name': 'Spot',
    'owner': 'Hank',
    'age': '6'
}

cat = {
    'name': 'Faith',
    'owner': 'Lauren',
    'age': '13'
}

pets = ['dog_0', 'dog_1', 'dog_2', 'cat']

for pet in pets:
    print(pet)

for animals, pet in pets.items():
    print(f"My name is {pet['name']}, my owner's name is {pet['owner']}.")
    print(f"I am {pet['age']} years old.")
