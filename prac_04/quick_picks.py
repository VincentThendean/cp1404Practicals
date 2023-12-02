import random

QUICK_PICK = []

def main():
    set_quick_pick()
    for picks in QUICK_PICK:
        for pick in picks:
            print(f"{pick:2}",end=" ")
        print()

def set_quick_pick():
    quick_pick_quantity = int(input("How many quick picks?: "))
    for i in range (quick_pick_quantity):
        QUICK_PICK.append(get_quick_pick())

def get_quick_pick():
    whole_line = []
    x = -1

    x = quick_pick_line()
    whole_line.append(x)

    for i in range (5):
        while x in whole_line:
            x = quick_pick_line()

        whole_line.append(x)

    whole_line.sort()

    return whole_line

def quick_pick_line():
    return random.randint(1,45)


main()
