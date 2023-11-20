"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
from random import randint


def main():
    user_score = float(input("Enter score: "))
    print(judge_score(user_score))
    print(judge_score(randint(0,100)))

def judge_score(user_score):
    if user_score > 100 or user_score < 0:
        return "Invalid Score"
    elif user_score <= 50:
        return "Bad"
    elif user_score <= 90:
        return "Passable"
    elif user_score <= 100:
        return "Excellent"


main()
