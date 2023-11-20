"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = get_tempCelsius()
            convert_CtoF(celsius)
        elif choice == "F":
            fahrenheit = get_tempFahrenheit()
            convert_FtoC(fahrenheit)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_FtoC(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"Result: {celsius:.2f} F")

def get_tempFahrenheit():
    fahrenheit = float(input("Fahrenheit: "))
    return fahrenheit


def convert_CtoF(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")

def get_tempCelsius():
    return float(input("Celsius: "))


main()

