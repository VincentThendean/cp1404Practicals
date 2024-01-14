
"""
My original car class did not return distance driven
"""

from random import randint

from car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        car_performance = randint(0, 100)
        if car_performance < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven

