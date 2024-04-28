from taxi import Taxi
# Create a new Taxi object without specifying price_per_km
my_taxi = Taxi("Prius 1", 100)
print(my_taxi)
my_taxi.drive(40)
print("After driving 40km:")
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")
my_taxi.drive(100)
print("After driving 100km:")
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")

