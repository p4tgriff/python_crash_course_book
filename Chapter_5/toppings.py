requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')


requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings


availabale_toppings = ['mushrooms', 'olives',
                       'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in availabale_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
