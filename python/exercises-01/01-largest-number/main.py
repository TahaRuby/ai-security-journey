#-----Method using Max and Min-----#
x = int(input("Enter how many numbers: ")) #  x represents the value entered by the user.
y = [] # y = list 

for i in range(x):
    number = int(input("Enter how many numbers: "))
    y.append(number) # i appended in y list

print("Numbers:", y)
print("Maximum:", max(y)) #  It prints the largest number.
print("Minimum:", min(y)) #  It prints the smaller number.

#-----Method without using Max and Min-----#

x = int(input("Enter how many numbers: "))

y = []

for i in range(x):
    y.append(int(input("Enter your number: ")))

maximum = y[0] #We set y to zero.
minimum = y[0] #We set y to zero.

for number in y: # We create a loop to compare the largest and smallest numbers.
    
    if number > maximum:
        maximum = number

    if number < minimum:
        minimum = number

print("Maximum:", maximum)
print("Minimum:", minimum)
