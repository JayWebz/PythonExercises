#! /usr/bin/python
# Exercise No.   2
# File Name:     hw3project2.py
# Programmer:    Jon Weber
# Date:          Sept. 10, 2017
#
# Problem Statement: Write a user-friendly program that calculates 
# both the quotient and the remainder of a division problem
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for a numerator
# 3. Prompt the user for a denominator
# 4. Print the resulting quotient and remainder
#
#
# import the necessary python libraries
# no libraries required

def main():
	print("Welcome to fractional calculator.")
	print("A program that is designed to calcuate the answer to a division problem.")

	print("Let's begin")

	#request numerator and denominator
	num = eval(input("List the numerator: "))
	den = eval(input("List the denominator: "))

	#calculate integer value and remainder value
	integer = num // den
	remainder = num % den

	#output result
	print ("The answer is", integer,"R",remainder)
		
main()
