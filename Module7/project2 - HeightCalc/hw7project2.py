#!   /usr/bin/python
#  Exercise No.   2
#  File Name:     hw7project2.py
#  Programmer: 	  Jon Weber
#  Date: 		  Oct. 8, 2017
#
#  Problem Statement: Write a program function that returns
#  the expected height of a child, based on it's gender and height of parents.
#
#
#  Overall Plan:
#  1. Greet User and prompt for gender 
#  2. Prompt user for height of parents
#  3. Calculate height based on gender input
#  4. Solve formula for child height with given parent height input
#  5. Output expected height of child
#
#  import the necessary python libraries
#  for this example none are needed

def maleChild(momHeight, dadHeight):
	#Apply formula to determine expected male height and print result in inches
	hMale = ((momHeight * 13/12) + dadHeight) / 2
	print("The expected height of the son will be", "%.1f" % hMale, "inches.")

def femaleChild(momHeight, dadHeight):
	#Apply formula to determine expected female height and print result in inches
	hFemale = ((dadHeight * 12/13) + momHeight) / 2
	print("The expected height of the daughter will be", "%.1f" % hFemale, "inches.")

def main():
	#Greet user
	print("This program will calculate the expected height of a child")
	print("When they become an adult. Let's begin:")
	#Request child gender and height of parents
	childGender = input("\nInput gender of child as 'm' or 'f'? \n")
	momHeight = eval(input("\nWhat is the height of the mother? \n"))
	dadHeight = eval(input("\nWhat is the height of the father? \n"))
	#run the proper formula given gender input. If invalid gender, return message
	if childGender == "m":
		maleChild(momHeight, dadHeight)

	elif childGender == "f":
		femaleChild(momHeight, dadHeight)
	else:
		print("Please input a valid gender")

main()
		