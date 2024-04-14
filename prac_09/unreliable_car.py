import random
from prac_06.car import Car
class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        chance = random.random() * 100

        # Check if the random number is less than the car's reliability
        if chance < self.reliability:
            # If the car is reliable enough, drive the requested distance
            return super().drive(distance)
        else:
            # If the car is not reliable, it doesn't move
            return 0


