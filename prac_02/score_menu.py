def main():

    score_range = [0,100]
    MENU = """
(G)et a valid score (must be 0-100)
(P)rint result
(S)how stars
(Q)uit
"""
    print(MENU)
    menu_choice = input('>')

    while menu_choice != "Q":
        if menu_choice == "G":
            user_score = set_userScore()
            while user_score < score_range[0] or user_score >score_range[1]:
                print('invalid')
                user_score = set_userScore()

        elif menu_choice == "P":
            get_userScore(user_score)

        elif menu_choice == "S":
            get_userScore_stars(user_score)

        else:
            print("Invalid command. Try again.")

        print(MENU)
        menu_choice = input('>')


def get_userScore_stars(userScore):
    print('*' * userScore)

def get_userScore(userScore):
    print(userScore)

def set_userScore():
    user_score = int(input('Input valid score (0-100):'))
    return user_score



main()