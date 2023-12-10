from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My guitars")

    guitar_name = str(input("Name: "))
    while guitar_name != "":
        add_new_guitar(guitar_name,guitars)
        guitar_name = str(input("Name: "))

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def add_new_guitar(guitar_name, guitars):
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: "))
    guitar_entry = Guitar(guitar_name, guitar_year, guitar_cost)
    guitars.append(guitar_entry)
    print(f"{guitar_entry} added.\n")


main()
