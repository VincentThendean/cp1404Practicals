numbers = []

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

def main():
    for i in range(5):
        numbers.append(set_numbers())

    get_first_number(numbers)
    get_last_number(numbers)
    get_smallest_number(numbers)
    get_largest_number(numbers)
    get_average_number(numbers)

def set_numbers():
    try:
        check_number = int(input("Number: "))
    except ValueError:
        print("Not a number")

    return check_number

def get_first_number(numbers):
    print(f"The first number is {numbers[0]}")

def get_last_number(numbers):
    print(f"The last number is {numbers[-1]}")

def get_smallest_number(numbers):
    print(f"The smallest number is {min(numbers)}")

def get_largest_number(numbers):
    print(f"The largest number is {max(numbers)}")

def get_average_number(numbers):
    average_number = (sum(numbers)/len(numbers))
    print(f"The average of the numbers is {int(average_number)}")

def main2():
    user_name = set_user_name()
    check_user_name(user_name)


def check_user_name(user_name):
    if user_name in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


def set_user_name():
    user_name = input("Username: ")
    return user_name


main2()