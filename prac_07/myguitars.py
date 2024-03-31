import csv
from prac_07.guitar import Guitar
def main():
    Guitars = []

    show_current_guitar(Guitars)
    add_new_guitars(Guitars)
    save_guitars(Guitars)
    print("Updated guitar list:")
    with open("guitars.csv", "r") as in_file:
        for line in in_file:
            print(line.strip())




def show_current_guitar(Guitars):
        with open("guitars.csv", "r") as in_file:
            for line in in_file:
                parts = line.strip().split(",")
                guitar = Guitar(parts[0], parts[1], parts[2])
                Guitars.append(guitar)

        sorted_guitars = sorted(Guitars)
        for guitar in sorted_guitars:
                print(guitar)

def add_new_guitars(Guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        Guitars.append(Guitar(name, year, cost))
        print(f"{guitar} added.")
        name = input("Name: ")


def save_guitars(Guitars):
    with open("guitars.csv", "w") as out_file:
        for guitar in Guitars:
                out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

main()