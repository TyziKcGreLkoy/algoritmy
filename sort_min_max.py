from random_generation import random_generator
from minimal_number_search import minimal_number_search
from search_biggest__with_index import biggest_number_search
from bubble_sort import bubble_sort

if __name__ == "__main__":
    spisok = random_generator(10, 0, 100)
    print(spisok)
    print(minimal_number_search(spisok))
    print(biggest_number_search(spisok))
    print(bubble_sort(spisok))

