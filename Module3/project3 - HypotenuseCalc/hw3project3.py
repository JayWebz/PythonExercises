#! /usr/bin/python
# Exercise No.   3
# File Name:     hw3project3.py
# Programmer:    Jon Weber
# Date:          Sept. 10, 2017
#
# Problem Statement: Write a user-friendly program that 
# determines the length of a ladder required to 
# reach a given height when leaned against a house
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for how high the ladder needs to go to access the spot to paint
# 3. Prompt the user for the angle the ladder will be resting at against the house
# 4. Use Sine function to determine hypotenuse of triangle, aka ladder length and return answer
#
#
# import the necessary python libraries
from math import * # Makes the math library available

def main():
	print("Welcome to Ladder Length Calculator.")
	print("A program that is designed to calcuate how long of a ladder is necessary to reach a spot on a wall.")

	print("Let's begin")
	#collect user inputs
	height = eval(input("List the height (in feet) of the spot to be accessed:"))
	degrees = eval(input("List the angle (in degrees) the ladder will placed at with the ground:"))
	#convert degrees to readian
	radian = (pi/180) * degrees
	#find the sine value of the radian calculated
	denominator = sin(radian)
	#find the hypotenuse with the now acquired denominator
	ladderLength = height / denominator
	#round the ladder value to two decimal places
	ladderLengthRounded = "%.2f" % ladderLength

	print("Your ladder will need to be at least", ladderLengthRounded, "feet long.")

main()
