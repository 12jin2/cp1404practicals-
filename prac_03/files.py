# 1.
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()
# 2.
in_file = open("name.txt", "r")
text = in_file.read()
in_file.close()
print(f"Your name is {text}")
# 3.
in_file = open("numbers.txt", "r")
line = in_file.readlines()
total_numbers = int(line[0]) + int(line[1])
print(total_numbers)
in_file.close()
# 4.
total_numbers = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total_numbers += int(line)
    print(total_numbers)