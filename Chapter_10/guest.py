filename = 'guest.txt'

with open(filename, 'a') as file_object:
    guest_name = input("What is your name?")
    file_object.write(f"{guest_name}.\n")


# guest_name = input("What is your name?")
