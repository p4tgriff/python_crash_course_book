prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."


# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# using break to exit a loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
