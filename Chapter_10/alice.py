filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents.read()
except FileNotFoundError:
    print(f'Sorry, the {filename} does not exist.')
