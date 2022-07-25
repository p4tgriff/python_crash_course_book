import json

username = input("What is your name?")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remmeber you when you come back, {username}!")
