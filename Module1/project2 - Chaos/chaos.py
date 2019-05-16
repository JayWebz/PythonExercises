#! /usr/bin/python
# Exercise No.   2
# File Name:     chaos.py
# Programmer:    Jon Weber
# Date:          Aug. 27, 2017
#
# Problem Statement: A simple program illustrating chaotic behaviour
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user a number between 0 and 1
# 3. Run the number through the formula on line 25. 
# 4. Loop through the output number of the formula ten times
#
#
# import the necessary python libraries
# for this example none are needed

def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number between 0 and 1: "))
	for i in range(10):
		x = 3.9 * x * (1 - x)
		print(x)

main()
