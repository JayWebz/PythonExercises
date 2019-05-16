#!   /usr/bin/python
#  Exercise No.   1
#  File Name:     hw7project1.py
#  Programmer: 	  Jon Weber
#  Date: 		  Oct. 8, 2017
#
#  Problem Statement: Write a program function that returns
#  the grade of a student, given a percentage
#
#
#  Overall Plan:
#  1. Greet User and request score percentage to convert into Letter Grade
#  2. Check to see if number entered is below 60, if so assign F
#  3. Check for each subsequent letter grade based on 10 point increments
#  4. After assigning a letter, return the letter grade to the user.  
#
#  import the necessary python libraries
#  for this example none are needed
	
def main():
	#Greet user
	print("This program will calculate the letter grade given a percentage score")
	print("Let's begin:")
	#Ask for percentage in class
	score = eval(input("\nWhat percentage do you have in your class? \n"))
	#Determine a letter grade to assign based on percentage
	if score < 60:
		print("Your grade for the class is an F.")
	elif score < 70:
		print("Your grade for the class is a D.")
	elif score < 80:
		print("Your grade for the class is a C.")
	elif score < 90:
		print("Your grade for the class is a B.")
	elif score < 100:
		print("Your grade for the class is an A.")
	#Determine if there is an edge case, print appropriate message if so.
	elif score > 100:
		print("Looks like you did extra credit! That's an A.")
	else:
		print("Invalid score given")
main()
		