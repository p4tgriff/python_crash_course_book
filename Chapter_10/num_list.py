# provided with a list provide the largest/smallest number.

my_list = [1, 2, 3, 4, 5, 6, 99, 245, 0]

# my_list.sort()
# print(my_list)


x = [0, 2, 3, 55, 79, 123, 5, 9, 11]
print("The largest number in this list is:", max(x))


def biggest_number():
    my_list.sort()
    print("The largest number in this list is: ", max(my_list))


biggest_number()


def guess_big_number(x=[]):
    # x = []
    x.sort()
    print("The largest number in THIS list is: ", max(x))


guess_big_number(1, 3, 5, 2)
