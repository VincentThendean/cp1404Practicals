import csv

from guitar import Guitar


def main():
    guitars = []

    set_guitars()

    insert_guitars_to_list(guitars)

    get_guitars(guitars)


def set_guitars():
    print("Add new guitars!")
    guitar_name = str(input("Name: "))
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))
        guitar_entry = f"\n{guitar_name},{guitar_year},{guitar_cost}"
        # guitar_entry = guitar_name + str(guitar_year) + str(guitar_cost)

        # print(guitar_entry)
        # break

        with open('guitars.csv', 'a') as out_file:
            out_file.write(guitar_entry)
        guitar_name = str(input("Name: "))


def get_guitars(guitars):
    for i in range(len(guitars)):
        print(guitars[i])


def insert_guitars_to_list(guitars):
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        guitar_list = line.strip().split(',')
        # print(guitar_list)
        guitar_entry = Guitar(guitar_list[0], guitar_list[1], guitar_list[2])

        guitars.append(guitar_entry)

    in_file.close()
    guitars.sort()


main()
