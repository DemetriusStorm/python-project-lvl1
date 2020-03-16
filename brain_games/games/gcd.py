from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def round():
    number_1 = randint(1, 20)
    number_2 = randint(1, 20)

    question = '{} {}'.format(number_1, number_2)

    if number_1 > number_2:
        number_1 %= number_2
    else:
        number_2 %= number_1

    right_solution = number_1 + number_2

    return question, str(right_solution)
