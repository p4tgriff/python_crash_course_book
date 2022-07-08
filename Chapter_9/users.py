class User:
    """Creating instances of a user."""

    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def describe_user(self):
        print(
            f'Here is what we know about {self.first_name} {self.last_name}.  Your username is {self.username} and your password is {self.password}.')

    def greet_user(self):
        print(
            f'Hello, {self.first_name}! The username {self.username} is a good fit for you.')


my_user = User('Brittni', 'Griffith', 'brich411', 'Ryder')
my_user.describe_user()

user_1 = User('Patrick', 'Griffith', 'bbyguy', 'house123')
user_1.greet_user()
