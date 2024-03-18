words = "This is Python"
print(words)

words = words.split()
print(words)

for word in words:
    print(word)
print([word for word in words])
 import csv
#
# with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
#     reader = csv.reader(in_file)  # Create a CSV reader to handle the file
#     next(reader)  # Skip the header row if your CSV has one
#     countries = []
#     champion_and_counts = {}
#
#     for line in reader:  # Process each line returned by the csv reader
#         champion = line[2].strip()  # Assuming the champion's name is in the second column
#         country = line[1].strip()
#         countries.append(country)
#         if champion in champion_and_counts:
#             champion_and_counts[champion] += 1
#         else:
#             champion_and_counts[champion] = 1
#
# print("Wimbledon Champions:")
# for champion, count in champion_and_counts.items():
#      print(f"{champion} {count}")
# print("These 12 countries have won Wimbledon:")
# print(",".join(sorted(countries)))