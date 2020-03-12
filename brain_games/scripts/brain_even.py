from random import randrange
from brain_games.cli import welcome_user, user_name
from brain_games.scripts.brain_games import welcome


def is_even():
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
    welcome()
    print('Answer "yes" if number even otherwise answer "no".')
    print()
    welcome_user()
    print()
    is_even()


if __name__ == '__main__':
    main()
