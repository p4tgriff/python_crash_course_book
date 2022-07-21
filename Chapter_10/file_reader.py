with open('py_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

filename = 'py_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents)

filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.replace('Python', 'C'))
