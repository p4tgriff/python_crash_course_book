def describe_pets(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")


describe_pets('hamster', 'Harry')
describe_pets('Belgian Malinois', 'Stella')
describe_pets(pet_name='Ryder', animal_type='pound puppy')
# describe_pets('Ryder', animal_type='pound puppy')
# describe_pets(pet_name='Ryder', 'pound puppy')
