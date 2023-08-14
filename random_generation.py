from random import randint


def random_generator(how_many, fromm, to):
    random_list = []
    for i in range(how_many):
        random_list.append(randint(fromm, to))
    return random_list


if __name__ == "__main__":
    how_many_ = int(input('Сколько чисел сгенерировать?'))
    fromm_ = int(input('От:'))
    to_ = int(input('До:'))
    print(random_generator(how_many_, fromm_, to_))
