import random
from brain_games.cli import check_answer, game_start, gratz, game_core


def is_prime(num):
    is_prime = 'yes'

    if num == 1:
        return 'no'

    for i in range(2, num):

        if num % i == 0:
            is_prime = 'no'
            break
    return is_prime


def brain_game_prime(name):
    i = 0
    result = True
    game_start('Answer "yes" if given number is prime. Otherwise answer "no".')

    while i < 3 and result:
        num = random.randint(1, 100)
        your_answer = game_core(num)

        if num == 2 or is_prime(num) == 'yes':
            correct_answer = 'yes'

        else:
            correct_answer = 'no'

        if not check_answer(correct_answer, your_answer, name):
            result = False
            break

        i += 1

    if result:
        gratz(name)
