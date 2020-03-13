from random import randrange
from brain_games.cli import welcome_user


def is_even():
    user_name = welcome_user()
    print()

    counter = 0

    while counter != 3:
        rnd_number = randrange(0, 100)
        question = 'Question: {}'.format(rnd_number)
        right_solution = 'yes' if rnd_number % 2 == 0 else 'no'

        print(question, right_solution)
        user_answer = input('Your answer: ')

        if user_answer == right_solution:
            counter += 1
            print('Correct!')
        else:
            print('\'{}\' is wrong answer ;(. Correct answer was \'{}\'.'
                  .format(user_answer, right_solution))
            print('Let\'s try again, {}!'.format(user_name))
            break

    if counter == 3:
        print('Congratulations, {}!'.format(user_name))


def main():
    print('be-Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    print()
    is_even()
