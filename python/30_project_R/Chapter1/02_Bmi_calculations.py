#imports and global variables


# getting user inputs as height and weight
def get_user_inputs():
    while True:
        try:
            weight = float(input("enter your weight (kg): "))
            height = float(input("enter your height (m): "))
        except ValueError:
            print("Please enter numbers only.\n")
            continue

        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than 0.\n")
            continue

        return weight, height


#calculate bmi
def calculate_bmi(weight, height):
    return weight / (height ** 2)   # "/" not "//" (// drops the decimals)


#get the bmi result
def get_bmi_result(bmi):
    print(f"bmi: {bmi:.1f}\nresult:")   # f-string so the value is really printed
    if bmi < 18.5:
        print("Under Weight")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Over Weight")
    elif bmi < 35:
        print("Obese")
    else:
        print("Extremely Obese")


#create main function to run
def main():
    weight, height = get_user_inputs()
    bmi = calculate_bmi(weight, height)
    get_bmi_result(bmi)


if __name__ == "__main__":
    main()