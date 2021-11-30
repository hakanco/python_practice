"""
Write a program for a first grader to practice additions.
The program should randomly generate two single-digit
integers number1 and number2 and display a question
such as “What is 7 + 9?” to the student. After the
student types the answer, the program should displays
a message to indicate whether the answer is true or false.
"""

import random

first_single_digit = random.randint(0, 9)
second_single_digit = random.randint(0, 9)

answer = int(input("What is the sum of {} and {}?".format(first_single_digit, second_single_digit)))

while answer != (first_single_digit + second_single_digit):
    print("Please, try again!")
    answer = int(input("What is the sum of {} and {}?".format(first_single_digit, second_single_digit)))


print("That is correct.")

