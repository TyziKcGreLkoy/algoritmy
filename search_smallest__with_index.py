from random_generation import random_generator


def minimal_number_search(number_list):
    maximum = number_list[0]
    for k in range(len(number_list)):
        if number_list[k] > maximum:
            maximum = number_list[k]
    return maximum


spisok = random_generator(10, 0, 100)
print(spisok)
print(minimal_number_search(spisok))
