#! /usr/bin/python
# Exercise No.   2
# File Name:     hw2project2.py
# Programmer:    Jon Weber
# Date:          Sept. 3, 2017
#
# Problem Statement: Write a user-friendly program that converts 
# Fahrenheit Temps into Celsius
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for a Fahrenheit Temperature
# 3. Calculate the conversion from Fahrenheit to Celsius
# 4. Round the converted number to the nearest tenth
# 5. Print the resulting Celsius number
#
#
# import the necessary python libraries
# for this example none are needed

def main():
	print("Welcome to Fahrenheit Converter.")
	print("A program that is designed to convert Fahrenheit to Celsius.")

	print("Let's get started")

	degreesF = eval(input("What is the Fahrenheit temperature? "))
	fahrLess32 = degreesF - 32
	degreesC = 5 * fahrLess32 /9
	degreesRoundedC = round(degreesC,1)
	conversion = "The temperature is", degreesRoundedC, "degrees Celsius."
	print(conversion)

main()
