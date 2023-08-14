from random_generation import random_generator


def bubble_sort(bubble_list):
    for j in range(len(bubble_list) - 1):
        for i in range(len(bubble_list) - 1):
            if bubble_list[i] > bubble_list[i + 1]:
                p = bubble_list[i + 1]
                bubble_list[i + 1] = bubble_list[i]
                bubble_list[i] = p
    return bubble_list


spisok = random_generator(10, 0, 100)
print(spisok)
print(bubble_sort(spisok))
