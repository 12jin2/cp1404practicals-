import random

MINIMUM_NUM = 1
MAXIMUM_NUM = 45

def main():
    num_quick_pick = int(input("How many quick picks? "))
    generate_quick_picks(num_quick_pick)

def generate_quick_pick():
    return sorted(random.randint(MINIMUM_NUM, MAXIMUM_NUM) for _ in range(6))

def generate_quick_picks(num_quick_pick):
    for _ in range(num_quick_pick):
        numbers = generate_quick_pick()
        print(" ".join(str(num) for num in numbers))


main()