import prompt


def run(game):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    print()

    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print()

    counter = 0
    all_count = 3

    while counter != all_count:
        question, right_solution = game.round()

        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')

        if user_answer == right_solution:
            counter += 1
            print('Correct!')
        else:
            print('\'{}\' is wrong answer ;(. Correct answer was \'{}\'.'
                  .format(user_answer, right_solution))
            print('Let\'s try again, {}!'.format(user_name))
            break

    if counter == all_count:
        print('Congratulations, {}!'.format(user_name))

