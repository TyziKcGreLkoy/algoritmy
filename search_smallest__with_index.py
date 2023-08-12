def minimal_number_search(number_list):
    maximum = number_list[0]
    for i in range(len(number_list)):
        if number_list[i] > maximum:
            maximum = number_list[i]
    return maximum


print(minimal_number_search([79, 95, 62, 42, 97, 23, 60, 66, 84, 37, 20, 80, 63, 82]))

