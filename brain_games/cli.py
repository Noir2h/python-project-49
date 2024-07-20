#!/usr/bin/env python3
import prompt


def welcome_user():
    print("welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def check_answer(correct_answer, your_answer, name):

    if correct_answer == your_answer:
        print("Correct!")
        return True

    else:
        print(f" '{your_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False


def game_start(rules, question):
    print(rules)
    print(f"Question: {question}")
    return prompt.string("Your answer: ")


def gratz(name):
    print(f"Congratulations, {name}!")