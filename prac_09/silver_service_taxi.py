from prac_09.taxi import Taxi
class SilverServiceTaxi(Taxi):
    flagfall = 4.50
    def __init__(self, name, fuel, fanciness):
        super().__init__(name,fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi, including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate and return the price for the taxi trip, including the flagfall."""
        return super().get_fare() + self.flagfall

    def start_fare(self):
        """Begin a new fare."""
        super().start_fare()
