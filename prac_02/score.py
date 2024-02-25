import random
def main():
    score = float(input("Enter score: "))
    get_result(score)
    show_random_result()
def get_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        if score >= 90:
             print("Excellent")
        elif score >= 50:
             print("Passable")
        else:
             print("Bad")

def show_random_result():
    random_score = random.randint(0,100)
    print(f"Random score = {random_score}")
    get_result(random_score)

main()
