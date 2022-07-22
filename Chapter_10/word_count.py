def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents.read()
    except FileNotFoundError:
        print(f'Sorry, the {filename} does not exist.')
        """pass would be acceptable if you didn't want to report the error but allow the program to continue unaffected."""
        # pass
    else:
        # Count the number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f'The file {filename} has  about {num_words} words.')


filename = 'alice.txt'
count_words(filename)
