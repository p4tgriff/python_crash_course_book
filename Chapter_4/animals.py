animals = ['monkey', 'cheetah', 'dog', 'cat']
for animal in animals:
    print(f'{animal.title()}s would be an awesome pet!\n')
print('These pets all have tails.')

# print first 3 in list
my_animals = animals[:3]

print('The first three items in this list are:')
print(my_animals)


# print middle 3 in list
my_animals = animals[1:4]

print('The middle three items in this list are:')
print(my_animals)


# print last 3 in list
my_animals = animals[-3:]

print('The final three items in this list are:')
print(my_animals)
