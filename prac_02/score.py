"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
from random import randint


def main():
    user_score = float(input("Enter score: "))
    print(judge_score(user_score))
    print(judge_score(randint(0, 100)))


def judge_score(user_score):
    excellent_score = 100
    passable_score = 90
    bad_score = 50
    score_range = [0, 100]

    if user_score < score_range[0] or user_score > score_range[1]:
        return "Invalid Score"
    elif user_score <= bad_score:
        return "Bad"
    elif user_score <= passable_score:
        return "Passable"
    elif user_score <= excellent_score:
        return "Excellent"


main()
