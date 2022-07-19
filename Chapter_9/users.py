class User:
    """Creating instances of a user."""

    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        print(
            f'Here is what we know about {self.first_name} {self.last_name}.  Your username is {self.username} and your password is {self.password}. You have logged in {self.login_attempts} number of times.')

    def greet_user(self):
        print(
            f'Hello, {self.first_name}! The username {self.username} is a good fit for you.')

    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    """A simple attempt at defining an admin role."""

    def __init__(self, first_name, last_name, username, password):
        """Initialize attributes of the parent class."""
        super().__init__(first_name, last_name, username, password)
        self.privileges = ['can add post',
                           'can delete a post', 'can ban a user']


# my_user = User('Brittni', 'Griffith', 'brich411', 'Ryder')
# my_user.describe_user()

# user_1 = User('Patrick', 'Griffith', 'bbyguy', 'house123')
# user_1.greet_user()

# my_user.increment_login_attempts(2)
# my_user.describe_user()
# my_user.reset_login_attempts()
# my_user.describe_user()
my_admin = Admin('Patrick', 'Griffith', 'p4tgriff', 'scoobydoo')
# print(my_admin.greet_user())
# print(my_admin.describe_user())
print(my_admin.privileges)
