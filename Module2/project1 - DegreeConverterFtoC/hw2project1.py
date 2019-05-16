#! /usr/bin/python
# Exercise No.   1
# File Name:     hw2project1.py
# Programmer:    Jon Weber
# Date:          Sept. 3, 2017
#
# Problem Statement: Write a user-friendly program that converts 
# Celsius Temps into Fahrenheit
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for a Celsius Temperature
# 3. Calculate the conversion from Celsius to Fahrenheit
# 4. Print the resulting Fahrenheit number
#
#
# import the necessary python libraries
# for this example none are needed

def main():
	print("Welcome to Celsius Converter.")
	print("A program that is designed to convert Celsius to Fahrenheit.")

	print("Let's get started")

	celsius = eval(input("What is the Celsius temperature? "))
	fahrenheit = 9/5 * celsius + 32
	print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()
