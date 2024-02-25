def main():

    password = get_password()
    print_password_asterisks(password)


def get_password ():
    password = input("Enter your password:")
    while len(password) < 5:
        print("The entered string is less than 5 characters long")
        password = input("Enter you password: ")
    return password
def print_password_asterisks(password):
    print("*" * len(password))
main()