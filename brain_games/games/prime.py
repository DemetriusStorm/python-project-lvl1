def is_prime(n):
    limit = (n ** 0.5)
    divider = 2
    while divider <= limit:
        if n % divider == 0:
            return False
        divider += 1
    return True


def round():
    n = randint(3, 100)
    question = str(n)
    right_solution = 'yes' if is_prime(n) else 'no'

    return question, right_solution
