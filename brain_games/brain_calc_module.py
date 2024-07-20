import random
from operator import add, sub, mul
from brain_games.cli import check_answer, game_start, gratz


def brain_calc_module(name):
    operations = (
        (mul, '*'),
        (sub, '-'),
        (add, '+'),
    )

    i = 0
    result = True

    while i < 3 and result:

        first_operand = random.randint(0, 10)
        second_operand = random.randint(0, 10)
        operations_random = random.choice(operations)
        operation, sign = operations_random
        correct_answer = operation(first_operand, second_operand)
        your_answer = game_start("What is the result of the expression?", f"{first_operand} {sign} {second_operand}",)

        if not check_answer(str(correct_answer), your_answer, name):
            result = False
            break

        i += 1

    if result:
        gratz(name)
