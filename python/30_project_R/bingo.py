#imports and global variables
import random

MAX_NUM = 10
MIN_NUM = 1
#Max_guess_counts = 3

#generate  a random number
def generate_random_num():
    return random.randint(MIN_NUM,MAX_NUM)


#get user input as  guess
def get_user_input():
    print(f"your number should be between {MIN_NUM}-{MAX_NUM}")

    while True:
        try:
            user_input = int(input("enter your guess: "))
        except ValueError :
            print("Error: enter  a valid number")
        else:
            return user_input

#check gusessed number

def ckeck_guessed_number(user_input,random_num):
    return user_input == random_num



#main function for running application
def main():
    Max_guess_counts = 3 
    random_num = generate_random_num()
    print(f"Random Number is:{random_num}")

    while Max_guess_counts >  0 :
        user_input = get_user_input()
        if ckeck_guessed_number(user_input,random_num):
            print("you have guessed right :O ")
            break
        Max_guess_counts -= 1 
        print(f"guesses left {Max_guess_counts}")
    else:
        print("you couldn't guess the number, and  ran out of guesses")

if __name__ == "__main__":
    main()    