#! /usr/bin/python
# Exercise No.   extra credit
# File Name:     hw3extraCredit.py
# Programmer:    Jon Weber
# Date:          Sept. 10, 2017
#
# Problem Statement: Write a user-friendly program that 
# prompts the user for a 4-digit year and then outputs the value of the Gregorian epact for that year
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for the year they want to find the epact for
# 3. solve for C, century
# 4. Use the epact formula to return an answer measured in days
#
#
# import the necessary python libraries
from math import * # Makes the math library available

def main():
	print("Welcome to Gregorian epact Calculator.")
	print("A program that is designed to calcuate how many days since the new moon come January 1st of a given year.")

	print("Let's begin")
	#collect user inputs
	year = eval(input("What year should we find the epact for? "))

	# find the century
	C = year // 100

	# break the formula into parts based on parentheses.
	paren1 = C // 4
	paren2 = 8 * C + 13
	paren3 = year % 19

	#plug in parenthetic variables to main equation
	epact = (8 + paren1 - C + (paren2 // 25) + 11 * paren3) % 30
	print("There were", epact, "days since the new moon on January 1st in", year)

main()
