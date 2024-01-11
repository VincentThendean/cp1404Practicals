from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    current_taxi = None
    current_bill = float(0.00)
    taxis = [Taxi("Prius", 100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = input(">>> ")
    menu_choice = menu_choice.lower()

    while menu_choice != "q":
        if menu_choice == "c":
            get_taxi_list(taxis)
            current_taxi = set_current_taxi(taxis)
            # print(current_taxi)
        elif menu_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                drive_taxi(current_taxi, taxis)
                current_bill = add_current_bill(current_bill, current_taxi, taxis)

        else:
            print("Invalid option")

        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input(">>> ")
        menu_choice = menu_choice.lower()

    print(f"Total trip cost: ${current_bill:.2f}")
    print("Taxis are now:")
    get_taxi_list(taxis)


def add_current_bill(current_bill, current_taxi, taxis):
    current_bill += taxis[current_taxi].get_fare()
    get_current_bill(current_bill)
    return current_bill


def drive_taxi(current_taxi, taxis):
    try:
        drive_distance = int(set_int(input("Drive how far? ")))
        taxis[current_taxi].drive(int(drive_distance))
        print(f"Your trip cost you ${taxis[current_taxi].get_fare():.2f}")
    except TypeError:
        return


def get_current_bill(current_bill):
    print(f"Bill to date: ${current_bill:.2f}")


def set_current_taxi(taxis):
    try:
        current_taxi = int(set_int(input("Choose taxi: ")))
        # current_taxi = -3
        taxis[current_taxi] = taxis[current_taxi]
        return current_taxi
    except IndexError:
        print("Invalid number")
    except TypeError:
        pass


def set_int(number):
    try:
        number = int(number)
        if number < 0:
            print("Number cannot be negative")
        else:
            return number
    except ValueError:
        print("Not a number")
    except TypeError:
        print("Error")


def get_taxi_list(taxis):
    for number, taxi in enumerate(taxis):
        print(f"{number} - {taxi}")


main()
