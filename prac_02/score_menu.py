def main():
    display_menu()
    score = int(input("Enter score: "))
    valid_score = get_a_valid_score(score)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
             score = int(input("Enter score: "))
             valid_score = get_a_valid_score(score)
        elif choice == "P":
             print_result(score)
        elif choice== "S":
             show_stars(score)
        else:
            print("Invalid option")
        display_menu()
        choice = input(">>> ").upper()
    print("Thank you.")







def display_menu():
    MENU = """(G)et a valid score
(P)rint result 
(S)how stars
(Q)uit"""
    print(MENU)

def get_a_valid_score(score):
    while score < 0  or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score
def print_result (score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def show_stars(score):
    for i in range(1,score + 1):
        print("*", end=' ')
main()