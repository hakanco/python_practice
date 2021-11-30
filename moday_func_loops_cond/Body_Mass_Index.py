"""Body Mass Index (BMI) is a measure of health on
weight. It can be calculated by taking your weight in
kilograms and dividing by the square of your height in
meters. The interpretation of BMI for people 16 years or
older is as follows:

BMI Interpretation

BMI < 18.5 Underweight
18.5 <= BMI < 25.0 Normal
25.0 <= BMI < 30.0 Overweight
30.0 <= BMI Obese
"""


def body_mass_index():
    age = int(input("Please enter your age: \n"))
    if age >= 16:
        weight = int(input("Please enter your weight in kilogram: "))
        height = float(input("Please enter your height in meters: "))
        BMI_value = weight / (height ** 2)
        print("Your BMI value is ", BMI_value)
        if BMI_value < 18.5:
            print("You are underweight. ")
        elif BMI_value < 25:
            print("You are normal. ")
        elif BMI_value < 30:
            print("You are overweight. ")
        else:
            print("You are obese. ")

    else:
        print("Sorry to inform you that this BMI calculation does not return result for the under age of 16.")


body_mass_index()

repeat = True
while repeat:
    print("Do you want to check one more time?")
    new_input = input("Please enter yes or no: ")
    if new_input in ["No", "NO", "no", "nO"]:
        repeat = False
        print("Have a nice day!")
    else:
        body_mass_index()
