alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

# print(alien_0)

print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_positon': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}.")

alien_0['speed'] = 'lightspeed'

# Move the position of the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# This must be a fast alien.

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}.")
