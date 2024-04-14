from prac_06.car import Car

from unreliable_car import UnreliableCar

def test_unreliable_car():
    # Create an UnreliableCar object with medium reliability
    my_car = UnreliableCar("RED", 100, 50)  # 50% reliability

    total_distance = 0
    # Attempt to drive the car 10 times, each time trying to drive 20 kilometers
    for i in range(10):
        distance_driven = my_car.drive(20)
        total_distance += distance_driven
        print(f"Attempted to drive 20km, drove {distance_driven}km.")

    print(f"Total distance driven after 10 attempts: {total_distance}km")

if __name__ == "__main__":
    test_unreliable_car()

