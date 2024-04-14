from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi
def main():
    MENU = """q)uit, c)hoose taxi, d)rive"""
    print("Let's drive!")
    total_cost = 0
    current_taxi = None
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    print(MENU)
    choice =input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            taxi_choice = input("Choose taxi: ")
            try:
                current_taxi = taxis[int(taxi_choice)]
            except (ValueError, IndexError):
                print("Invalid taxi choice")
            print(f"Bill to date: ${total_cost:.2f}")
        elif choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_cost += trip_cost
            print(f"Bill to date: ${total_cost:.2f}")
        else:
            print("Invalid option")
            print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        choice = input(">>>").upper()
    print(f"Total trip cost: ${total_cost}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()