import random
from brain_games.cli import check_answer, game_start, gratz, game_core


def progression():
    my_list = []
    start_progression = random.randint(1, 10)
    step_progression = random.randint(1, 5)
    count_progression = random.randint(5, 10)
    end_progression = start_progression
    missed = '..'
    i = 0
    while i < count_progression:
        end_progression += step_progression
        i += 1

    for i in range(start_progression, end_progression, step_progression):
        my_list.append(str(i))

    element_for_change = random.randint(0, len(my_list) - 1)
    answer = my_list[element_for_change]
    my_list[element_for_change] = missed

    return my_list, answer


def progression_game(name):
    i = 0
    result = True
    game_start("What number is missing in the progression?")

    while i < 3 and result:
        game_progression, correct_answer = progression()
        your_answer = game_core({" ".join(game_progression)})

        if not check_answer(correct_answer, your_answer, name):
            result = False
            break

        i += 1

    if result:
        gratz(name)
