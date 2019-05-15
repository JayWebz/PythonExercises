#! /usr/bin/python
# Exercise No.   1
# File Name:     MyFirstProgram.py
# Programmer:    Jon Weber
# Date:          Aug. 27, 2017
#
# Problem Statement: Ask the user to enter three numbers, calculate the sum of 
# these three numbers, and display the sum to the screen
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for three integers
# 3. Calculate the sum of the integers
# 4. Print the sum of the integers to the screen
# 5. Calculate the product of the integers
# 6. Print the product of the integers to the screen
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print a message to the screen
    print("Hello!")
    print("I can add and multiply three numbers for you")

    # Variables are declared dynamically no need to pre-define
    num1 = eval(input("Enter one whole number(Ex. 52):"))
    num2 = eval(input("Enter another whole number(Ex. 41):"))
    num3 = eval(input("Enter an additional third number(Ex. 24):"))

    print("The first number selected:", num1)
    print("The second number selected:", num2)
    print("The third number selected:", num3)

    percentage = (num1 / num2 ) * 100
    print("Percentage = ", percentage)

    #Here is the processing that is needed
    sum = num1 + num2 + num3
    product = num1 * num2 * num3

    # Output the results
    print("The sum of the three numbers is", sum)
    print("The product of the three numbers is", product)

main()

