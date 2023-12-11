import csv

from guitar import Guitar


def main():
    guitars = []

    in_file = open('guitars.csv', 'r')

    for line in in_file:
        guitar_list = line.strip().split(',')
        # print(guitar_list)

        guitar_entry = Guitar(guitar_list[0], guitar_list[1], guitar_list[2])
        # print(guitar_entry)

        guitars.append(guitar_entry)

    in_file.close()

    guitars.sort()

    for i in range(len(guitars)):
        print(guitars[i])


main()
