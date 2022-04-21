pizzas = ['pepperoni', 'cheese', 'jalepeno']
for pizza in pizzas:
    print(f'I love {pizza.lower()} pizza!\n')

friend_pizzas = pizzas[:]

pizzas.append('sausage')
print(pizzas)

friend_pizzas.append('pinneapple')
print(friend_pizzas)

print('My favorite pizzas are:')
print(pizzas)

# Error here! This should print only 1 item from the list then iterate to the next.
for pizza in friend_pizzas:
    print(f'My friends favorite pizzas are: {friend_pizzas}\n')
