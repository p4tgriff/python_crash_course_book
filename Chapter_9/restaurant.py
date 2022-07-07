class Restaurant:
    """An attempt to model a restaurant."""

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(
            f'My restaurant has multiple types of cuisine, including: {self.type}')

    def open_restaurant(self):
        print(f'{self.name} is open for business.')


my_restaurant = Restaurant('Johnnys', 'pizza')

print(f'My favorite restaurant is {my_restaurant.name}.')
print(f'\nThey are a {my_restaurant.type} place.')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
