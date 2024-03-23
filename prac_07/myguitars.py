import csv
from prac_07.guitar import Guitar
def main():


        Guitars = []
        with open("guitars.csv", "r") as in_file:
            for line in in_file:
                parts = line.strip().split(",")
                guitar = Guitar(parts[0], parts[1], parts[2])
                Guitars.append(guitar)

        sorted_guitars = sorted(Guitars)
        for guitar in sorted_guitars:
                print(guitar)

main()