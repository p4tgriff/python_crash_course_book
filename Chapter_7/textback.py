# message = input("Tell me something and I'll repeat it back to you: ")
# print(message)

car = input("What kind of rental car would you like today? ")
car = car

if car == 'Toyota':
    print("Yes, we have a Toyota for you.")
else:
    print("Sorry, we only have a Toyota for you today!")


table = input("How many people are in your dinner party? ")
table = int(table)

if table >= 8:
    print("Due to your party size, there will be a 15 minute wait.")
else:
    print("Your table is ready now.")

multiple_of_ten = input(
    "Provide me with a number and I'll tell you if it's a multiple of ten. ")
