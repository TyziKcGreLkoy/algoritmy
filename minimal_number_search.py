def minimal_number_search(number_list):
    minimal = number_list[0]
    for i in number_list:
        if i < minimal:
            minimal = i
    return minimal


print(minimal_number_search([79, 95, 62, 42, 97, 23, 60, 66, 84, 37, 20, 80, 63, 82, ]))



