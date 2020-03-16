from random import randint

DESCRIPTION = "What number is missing in the progression?"


def round():
    start_seq = randint(1, 100)
    step_seq = randint(1, 10)
    guess_element = randint(1, 10)

    question = str(start_seq)
    right_solution = ''

    for element in range(10):
        start_seq += step_seq

        if element != guess_element - 1:
            question += ' ' + str(start_seq)
        else:
            right_solution = str(start_seq)
            question += ' ...'

    return question, right_solution
