#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.brain_even_module import brain_even_game
from brain_games.brain_nod_module import brain_nod_func
from brain_games.games_is_prime import brain_game_prime
from brain_games.brain_game_progression_module import progression_game
from brain_games.brain_calc_module import brain_calc_module


def main():
    welcome_user()


def brain_even():
    name = welcome_user()
    brain_even_game(name)


def brain_gcd():
    name = welcome_user()
    brain_nod_func(name)


def brain_prime():
    name = welcome_user()
    brain_game_prime(name)


def brain_progression():
    name = welcome_user()
    progression_game(name)


def brain_calc():
    name = welcome_user()
    brain_calc_module(name)


if __name__ == '__main__':
    main()
