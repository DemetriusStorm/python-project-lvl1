from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even():
    question = randint(1, 100)

    if question % 2 == 0:
        right_solution = 'yes'
    else:
        right_solution = 'no'

    return str(question), right_solution
