from  random_generation import random_generator


def quick_sort(num):
    if len(num) < 2:
        return num
    else:
        pivot = num[0]
        less = [i for i in num[1:] if i < pivot]

        greater = [i for i in num[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


numbers = random_generator(10, 0, 50)
print(numbers)
print(quick_sort(numbers))