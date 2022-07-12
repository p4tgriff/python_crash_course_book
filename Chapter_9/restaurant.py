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

    def set_number_served(self, number):
        self.customer_number = number
        print(f'Now serivce custmer {self.number}!')

    def increment_number_server(self,):
        print(f'')


my_restaurant = Restaurant('Johnnys', 'pizza')

print(f'My favorite restaurant is {my_restaurant.name}.')
print(f'\nThey are a {my_restaurant.type} place.')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.customer_number = 3
my_restaurant.current_customer()
