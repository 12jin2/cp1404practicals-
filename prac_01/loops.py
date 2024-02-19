#A.
for i in range(0, 101, 10):
    print(i, end=' ')
print()
#b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()
#c.
numbers = int(input("Enter numbers: "))
for stars in range(1, numbers + 1):
    print("*", end=' ')
print()
#d.
numbers = int(input("Enter numbers: "))
for row in range(1, numbers + 1):
    print("*" * row)

