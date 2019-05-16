#! /usr/bin/python
# Exercise No.   1
# File Name:     hw3project1.py
# Programmer:    Jon Weber
# Date:          Sept. 10, 2017
#
# Problem Statement: Write a user-friendly program that calculates 
# the cost per square inch of a circular pizza
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for the size of the pizza
# 3. Prompt the user for the cost of the pizza
# 4. Print the resulting Fahrenheit number
#
#
# import the necessary python libraries
from math import * # Makes the math library available

def main():
	print("Welcome to Pizza Cost Analyzer.")
	print("A program that is designed to calcuate how much a pizza costs per square inch.")

	print("Let's begin")

	#calcuate the area
	#request diameter input
	pizzaDia = eval(input("What is the diameter of the pizza in inches? "))
	#calcuate and print the area
	pizzaDiaSquared = pizzaDia ** 2
	pizzaArea = pi*pizzaDiaSquared
	print("Based on a diameter of ", pizzaDia, "it looks like that pizza is", pizzaArea, "square inches.")

	#request price input
	pizzaPri = eval(input("Now, how much does the pizza cost? "))
	#calcuate pricing per square inch
	value = pizzaPri / pizzaArea

	#round the value to the nearest cent
	valueDollars = "%.2f" % value
	print("This pizza costs $",valueDollars, "dollars per square inch.")
		
main()
