# import variable 

#create function 
# create function
def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

#running application 
def main():
    print(10*"==")
    Userinput=input("Enter your string:")
    print(10*"==")
    if is_palindrome(Userinput):       
        print("The string is  a palindrome")       
    else:       
        print("The string is not a plindrome")

main()