def main():

    MENU = """
(G)et a valid score (must be 0-100)
(P)rint result
(S)how stars
(Q)uit
"""
    print(MENU)
    menuChoice = input('>')
    while menuChoice != "Q":
        if menuChoice == "G":
            userScore = set_userScore()
            while userScore < 0 or userScore >100:
                print('invalid')
                userScore = set_userScore()

        elif menuChoice == "P":
            get_userScore(userScore)

        elif menuChoice == "S":
            get_userScore_stars(userScore)

        else:
            print("Invalid command. Try again.")

        print(MENU)
        menuChoice = input('>')


def get_userScore_stars(userScore):
    print('*' * userScore)

def get_userScore(userScore):
    print(userScore)

def set_userScore():
    enteredscore = int(input('Input valid score (0-100):'))
    return enteredscore



main()