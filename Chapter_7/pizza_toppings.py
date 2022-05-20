# Write a while loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.  As they enter each topping, print a message saying you'll add that topping to their pizza.

prompt = "Please enter the toppings that you'd like on your pizza."
prompt += "\n(Please type 'quit' to exit.)"

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(f"I've added {toppings.title()} to your pizza!")


# Write a while loop that expresses someone's age and their applicable movie ticket price.  >3 = free, 3-12 = $10, 12+ = $15.

prompt = "\nPlease tell me your age and I will let you know the cost of your ticket."
prompt += "\n(Please type 'quit' to exit.)"

while True:
    age = input(prompt)

    if age == 'quit':
        break
    if age >= '3':
        print("Your ticket is $10.")
        break
    if age >= '12':
        print("Your ticket is $15.")
        break
    else:
        print("Your ticket is Free!")
