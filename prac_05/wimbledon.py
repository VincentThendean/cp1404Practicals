"""
Wimbledon
Estimate: 60 minutes
Actual:   52 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    matches = []
    winners_dictionary = {}
    winning_country = []

    process_winner_table(matches, winners_dictionary, winning_country)

    get_winners_dictionary(winners_dictionary)

    get_winning_country(winning_country)


def get_winning_country(winning_country):
    print(f"These {len(winning_country)} countries have won Wimbledon:")
    print(", ".join(winning_country))


def get_winners_dictionary(winners_dictionary):
    print("Wimbledon Champions:")
    for key, value in winners_dictionary.items():
        print(f"{key} {value}")
    print()


def process_winner_table(matches, winners_dictionary, winning_country):
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            matches.append(line.strip())
        del matches[0]

        for match in matches:
            game = match.split(',')

            if game[1] not in winning_country:
                winning_country.append(game[1])

            if game[2] in winners_dictionary.keys():
                winners_dictionary[game[2]] += 1
            else:
                winners_dictionary[game[2]] = 1
    winning_country.sort()


main()
