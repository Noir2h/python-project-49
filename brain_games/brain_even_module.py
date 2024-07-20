import random
from brain_games.cli import check_answer, game_start, gratz, game_core


def brain_even_game(name):
    i = 0
    result = True
    game_start('Answer "yes" if the number is even, otherwise answer "no".')

    while i < 3 and result:
        question_about_even = random.randint(0, 100)
        your_answer = game_core(question_about_even)

        if question_about_even % 2 == 0:
            correct_answer = "yes"

        else:
            correct_answer = 'no'

        if not check_answer(correct_answer, your_answer, name):
            result = False
            break

        i += 1

    if result:
        gratz(name)
