def main():
    email_and_name = {}
    email = input("Email: ").strip()

    while email != "":

        name_parts = email.split("@")[0]
        proposed_name = ' '.join(name_parts.split('.')).title()  # Note: Changed variable name for clarity
        print(proposed_name)


        choice = input(f"Is your name {proposed_name}? (Y/n) ").upper()
        if choice == "Y" or choice == "":
            email_and_name[email] = proposed_name
        else:
            corrected_name = input("Name: ").strip().title()
            email_and_name[email] = corrected_name


        email = input("Email: ").strip()


    for email, name in email_and_name.items():
        print(f"{name} ({email})")


main()