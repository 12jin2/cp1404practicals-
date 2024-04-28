from prac_09.silver_service_taxi import SilverServiceTaxi
def test_silver_service_taxi():
      new_taxi = SilverServiceTaxi("Red", 20, 2)
      print(new_taxi)
      new_taxi.drive(18)
      print("After driving 18km:")
      print(new_taxi)
      print(f"Fare for 18km trip: ${SilverServiceTaxi.get_fare(new_taxi):.2f}")



test_silver_service_taxi()