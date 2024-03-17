
import csv


def read_data(filename):
    """Read data from CSV and return as a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)
        return [line for line in reader]


def count_champions(data):
    """Return a dictionary with champions and their win counts."""
    champion_and_counts = {}
    for line in data:
        champion = line[2].strip()
        if champion in champion_and_counts:
            champion_and_counts[champion] += 1
        else:
            champion_and_counts[champion] = 1
    return champion_and_counts


def extract_countries(data):
    """Return a set of unique countries."""
    return {line[1].strip() for line in data}


def main():

    filename = "wimbledon.csv"
    wimbledon_data = read_data(filename)
    champion_and_counts = count_champions(wimbledon_data)

    countries = extract_countries(wimbledon_data)
    print("Wimbledon Champions:")
    for champion, count in champion_and_counts.items():
        print(f"{champion} {count}")
    print()
    print("These countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()