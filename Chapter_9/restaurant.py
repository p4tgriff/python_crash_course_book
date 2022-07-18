class Restaurant:
    """An attempt to model a restaurant."""

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.customer_number = 0

    def describe_restaurant(self):
        print(
            f'My restaurant has multiple types of cuisine, including: {self.type}')

    def open_restaurant(self):
        print(f'{self.name} is open for business.')

    def current_customer(self):
        print(f'Now serving customer number {self.customer_number}.')

    def set_number_served(self):
        print(f'We have serverd {self.customer_number} customers today.')

    def increment_number_served(self, numbers):
        self.customer_number += numbers


my_restaurant = Restaurant('Johnnys', 'pizza')

print(f'My favorite restaurant is {my_restaurant.name}.')
print(f'\nThey are a {my_restaurant.type} place.')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.customer_number = 3
my_restaurant.current_customer()

my_restaurant.set_number_served()
my_restaurant.increment_number_served(10)
my_restaurant.current_customer()


class IceCream:
    """A simple attempt to model ice cream as a treat."""

    def __init__(self, flavors='chocolate'):
        self.flavors = flavors

    def list_of_flavors(self):
        print(f'This is our list of flavors: {self.flavors}.')


class IceCreamStand(Restaurant):
    """An attempt to model an ice cream store."""

    def __init__(self, name, type):
        """Initial attributes of the parent class."""
        super().__init__(name, type)
        self.IceCream = IceCream()

    def flavors(self):
        """An attribute that's for ice cream flavors."""
        self.strawberry = strawberry
        self.banana = banana
        self.vanilla = vanilla
        self.chocolate = chocolate

    def flavors_list(self):
        flavor_list = f'{self.strawberry}, {self.banana}, {self.vanilla}, {self.chocolate}.'
        print('flavor_list.title()')


ice_cream_palace = IceCreamStand('Patricks Ice Cream Palace', 'ice cream')
print(ice_cream_palace.IceCream.flavors)
