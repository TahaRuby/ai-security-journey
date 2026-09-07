#imports and global variables
import random

USER_COICES = ["rock","paper","scissors"]

#crate function to get user input
def get_user_input():
    choice = input("pick your choice:[\"rock\",\"paper\",\"scissor\"]\t")
    while choice not  in USER_COICES:
        choice = input("pick your choice:[\"rock\",\"paper\",\"scissor\"]\t")
        return choice


#create a function  to get pc input
def get_pc_input():
    pc_choice = random.choice(USER_COICES)
    print(f"pc choice was: {pc_choice}")
    return pc_choice


# compare and  datermine which one is the winner
def determine_winner(user_input,pc_input):
    if user_input == pc_input:
        return "DRAW!"
    elif user_input == "rock" and (pc_input == "scissor") or \
        user_input == "scissor" and (pc_input == "papar") or \
            user_input == "paper" and (pc_input == "rock"):
        print("user won")
    else :
        print("computer won")


# create  a main function as the runner
def main():
    user_input = get_user_input()
    pc_input = get_pc_input()
    determine_winner(user_input,pc_input)
    print("end of program")

main()


#make an iteration for  doing the game  as  much as we need
answer = "y"

while answer=="y":
    main()
    answer = input("do you want to continue? (y/n):")
