#! /usr/bin/python
# Exercise No.   3
# File Name:     hw2project3.py
# Programmer:    Jon Weber
# Date:          Sept. 3, 2017
#
# Problem Statement: Write a user-friendly program that  
# finds the average score of exams
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for how many numbers they want to find the average of
# 3. Prompt the user for the values that they want to average out
# 4. Loop through the values given to find the sum of all values
# 5. divide the sum by the number of inputs
# 6. Print the resulting average number
#
#
# import the necessary python libraries
# for this example none are needed

def main():
	print("Welcome to The Exam Score Average Finder.")
	print("A program that is designed to find the average of exam scores.")

	print("Let's get started...")

	valueQty = eval(input("Enter how many exam scores will be averaged: "))
	valuesToAvg = eval(input("List the exam scores seperated by comma(,): "))
	sum = 0
	for i in range(valueQty) :
		sum = sum + valuesToAvg[i]
	average = sum / valueQty
	print ("Your average exam score is: ", average)
main()
