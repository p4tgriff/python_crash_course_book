for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

odd_numbers = list(range(1, 7, 2))
print(odd_numbers)

squares = []
for value in range(1, 11):
    # square = value ** 2
    squares.append(value**2)

print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))
print(sum(digits))
print(min(digits))

# count to 20
for number in range(1, 21):
    print(number)

# count to 1 million
# for number in range(1, 1000001):
#     print(number)

# odd numbers only
for number in range(1, 21, 2):
    print(number)

# 3-30
for number in range(3, 31, 3):
    print(number)

# cubed list 1-10
cubes = []
for value in range(1, 11):
    cubed = value ** 3
    cubes.append(cubed)

print(cubed)

cubes = [value**3 for value in range(1, 11)]
print(cubes)
