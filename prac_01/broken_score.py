"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score > 100 or score < 0:
    print("Invalid Score")
elif score <= 50:
    print("Bad")
elif score <= 90:
    print("Passable")
elif score <= 100:
    print("Excellent")
