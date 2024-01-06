from car import Car
from unreliable_car import UnreliableCar


def main():
    old_car = UnreliableCar("Ford Pinto", 100, 40)

    for i in range(5):
        old_car.drive(20)
        print(old_car)




main()