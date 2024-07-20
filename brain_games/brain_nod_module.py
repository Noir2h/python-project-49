from brain_games.cli import check_answer, game_start, gratz_user, game_core
from math import gcd
import random


def brain_nod_func(name):
    i = 0
    result = True
    game_start("Find the greatest common divisor of given numbers.")
    while i < 3 and result:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        correct_answer = gcd(first_number, second_number)
        your_answer = game_core(f"{first_number} {second_number}")

        if not check_answer(str(correct_answer), your_answer, name):
            result = False
            break

        i += 1

    if result:
        gratz_user(name)
