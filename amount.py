from random_generation import random_generator


def amount(num):
    if num == []:
        return 0
    else:
        return num[0] + amount(num[1:])


numbers = random_generator(10, 0, 50)
print(numbers)
print(amount(numbers))
