from random import randint, choice
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'


def round():
    number_1, number_2 = randint(1, 10), randint(1, 10)
    list_operations = [('+', add), ('-', sub), ('*', mul)]
    operation, function = choice(list_operations)
    question = '{} {} {}'.format(number_1, operation, number_2)
    right_solution = function(number_1, number_2)

    return question, str(right_solution)
