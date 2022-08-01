# provided with a list provide the largest/smallest number.

my_list = [1, 2, 3, 4, 5, 6, 99, 245, 0]
y = []

# my_list.sort()
# print(my_list)


x = [0, 2, 3, 55, 79, 123, 5, 9, 11]
print("The largest number in this list is:", max(x))


def biggest_number():
    print("The largest number in this list is: ", max(my_list))


biggest_number()


# def guess_big_number():
#     x = []
#     x.sort()
#     print("The largest number in THIS list is: ", max(x))


# guess_big_number()


def last_num():
    print(x[-1])
    if y == []:
        print("There is nothing here.")
    else:
        print(y)


last_num()
