"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
from random import randint


def main():
    score = float(input("Enter score: "))
    print(judge_score(score))
    print(judge_score(randint(0,100)))

def judge_score(score):
    if score > 100 or score < 0:
        return "Invalid Score"
    elif score <= 50:
        return "Bad"
    elif score <= 90:
        return "Passable"
    elif score <= 100:
        return "Excellent"


main()
