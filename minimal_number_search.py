from random_generation import random_generator


def minimal_number_search(number_list):
    minimal = number_list[0]
    for i in number_list:
        if i < minimal:
            minimal = i
    return minimal


spisok = random_generator(10, 0, 100)
print(spisok)
print(minimal_number_search(spisok))

