from random import choice
from random import randint
print(randint(1, 6))


class Die:
    """A simulation of a single die."""

    def roll_die():
        print(randint(1, 6))


Die.roll_die()

numbers_list = ['1', '2', '3', '4', '5', '6',
                '7', '8', '9', '10', 'A', 'B', 'C', 'D', 'E']

pick_5 = choice(numbers_list)
print(pick_5)
