#! /usr/bin/python
# Exercise No.   1
# File Name:     hw8project1.py
# Programmer:    Jon Weber
# Date:          Oct. 22, 2017
#
# Problem Statement: Create a program that computes
# and outputs the nth Fibonacci number, where n is a 
# value entered by the user.
#
# Overall Plan:
# 1. Greet User and request nth value desired from Fibonacci Sequence
# 2. Initialize values needed for calculations
# 3. Check for valid input from user
# 4. Loop through calculations until the number of loops equals the user input
# 5. Print the value from the Fibonacci Sequence that coorelates to the user input
#
# import the necessary python libraries
# no libraries necessary

def main():
	#Greet user
	print("\nThis program will find a desired value of the Fibonacci Sequence.")
	print("Please have a value in mind of which position in the sequence you'd like to see.\n")
	print("Let's Begin:\n")
	try:
		# Request position number from user
		n = eval(input("What position do you want the value from the Fibonacci sequence? "))
		# Initialize sum, count, and previous two numbers that make up sum
		sum = 1
		count = 1
		prev2 = 0
		prev1 = 1
		# Check if n is both positive and a whole number
		if n > 0 and type(n) == int:
			# perform loop until the loop count is equal to user input
			while n > count:
				# If n = 1 then print initialized sum
				if n == 1:
					break
				# Find next value in sequence based on count
				else:
					# Add previous numbers together to get sum
					sum = prev2 + prev1
					# Reset values for previous numbers based on new sum
					prev2 = prev1
					prev1 = sum	
					# Add 1 to count
					count = count + 1	
			# When count = n, print the number that's in the nth position of sequence
			print("The value at position ", n, " in", sep="")
			print("the Fibonacci Sequence is", sum)
		# Return message if number entered is not positive
		else:
			print("Please input a positive whole number.")
	# Return message if input is not integer
	except:
		print("Please input integer.")
main()
