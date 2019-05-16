#! /usr/bin/python
# Exercise No.   3
# File Name:     quarterback.py
# Programmer:    Jon Weber
# Date:          Aug. 27, 2017
#
# Problem Statement: Write a program that computes 
# the completion percentage for a quarterback.  
# Your input will be pass completions and pass attempts.
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for two integers
# 3. Calculate the quotient of the integers
# 4. Print the quotient of the integers to the screen
#
#
# import the necessary python libraries
# for this example none are needed

def main():
    print("This program calculates the completion percentage for a QB")
    num1 = eval(input("Enter the number of passes completed: "))
    num2 = eval(input("Enter the number of passes attempted: "))

    percentage = (num1 / float(num2)) * 100
    print("Percentage = ", percentage)

main()
