from car import Car
from taxi import Taxi


class SilverServiceTaxi(Taxi):

    def __init__(self, fanciness, **kwargs):
        # super().__init__(name, fuel)
        super().__init__(**kwargs)
        self.price_per_km = fanciness * Taxi.price_per_km
        self.flagfall = 4.50

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance + self.flagfall
