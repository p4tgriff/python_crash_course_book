alien_colors = 'red'

if 'green' in alien_colors:
    print('Player 1 just earned 5 points!')

if 'red' in alien_colors:
    print('Player 1 just earned 5 points!')

if 'green' in alien_colors:
    print('Player 1 just earned 5 points!')

elif 'yellow' in alien_colors:
    print('Player 1 just earned 10 points!')

elif 'red' in alien_colors:
    print('Player 1 just earned 15 points!')


stage_of_life = 1

# if '0' > stage_of_life:
#     print('This person is a baby.')

# elif '2' > stage_of_life:
#     print('This person is a toddler.')

# elif '4' > stage_of_life:
#     print('This person is a kid.')

# elif '13' > stage_of_life:
#     print('This person is a teenager.')

# elif '20' > stage_of_life:
#     print('This person is a adult.')

# elif '65' > stage_of_life:
#     print('This person is an elder.')


if stage_of_life < 2:
    name = 'baby'

elif stage_of_life < 4:
    name = 'toddler'

elif stage_of_life < 13:
    name = 'kid'

elif stage_of_life < 20:
    name = 'teenager'

elif stage_of_life < 65:
    name = 'adult'

else:
    name = 'elder'

print(f"This person is a {name}.")
