def main():
    numbers = []
    numbers = get_number(numbers)

    output_imformation(numbers)


def get_number(numbers):
    for i in range(1, 6):
         number = int(input("Number: "))
         numbers.append(number)
    return numbers

def output_imformation(numbers):
    print(f"The first number is {numbers[0]} ")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers)/len(numbers)}")
main()

def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access Denied")

main()
