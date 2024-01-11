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
            set_current_taxi(taxis)
            get_current_bill(current_bill)

        else:
            print("Invalid option")

        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input(">>> ")
        menu_choice = menu_choice.lower()


def get_current_bill(current_bill):
    print(f"Bill to date: ${current_bill:.2f}")


def set_current_taxi(taxis):
    try:
        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
    except ValueError:
        print("Not a number")
    except IndexError:
        print("Invalid number")
    except:
        print("Error")


def get_taxi_list(taxis):
    for number, taxi in enumerate(taxis):
        print(f"{number} - {taxi}")


main()
