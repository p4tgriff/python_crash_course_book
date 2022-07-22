filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents.read()
except FileNotFoundError:
    print(f'Sorry, the {filename} does not exist.')
else:
    # Count the number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f'The file {filename} has  about {num_words} words.')
