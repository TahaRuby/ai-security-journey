#imports and global variables
import random

CHOICES = ["rock", "paper", "scissors"]


#create function to get user input
def get_user_input():
    choice = input('pick your choice ["rock", "paper", "scissors"]:\t').strip().lower()
    while choice not in CHOICES:
        print("Invalid choice, try again.")
        choice = input('pick your choice ["rock", "paper", "scissors"]:\t').strip().lower()
    return choice   # outside the while loop (this was the bug)


#create a function to get pc input
def get_pc_input():
    pc_choice = random.choice(CHOICES)
    print(f"pc choice was: {pc_choice}")
    return pc_choice


# compare and determine which one is the winner
def determine_winner(user_input, pc_input):
    if user_input == pc_input:
        print("DRAW!")
    elif (user_input == "rock" and pc_input == "scissors") or \
         (user_input == "scissors" and pc_input == "paper") or \
         (user_input == "paper" and pc_input == "rock"):
        print("user won")
    else:
        print("computer won")


# create a main function as the runner
def main():
    user_input = get_user_input()
    pc_input = get_pc_input()
    determine_winner(user_input, pc_input)
    print("end of round")


# play as many rounds as we want
if __name__ == "__main__":
    answer = "y"
    while answer == "y":
        main()
        answer = input("do you want to continue? (y/n): ").strip().lower()