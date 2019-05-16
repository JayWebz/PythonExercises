#!   /usr/bin/python
#  Exercise No.   2
#  File Name:     hw6project2.py
#  Programmer: 	  Jon Weber
#  Date: 		  Oct. 1, 2017
#
#  Problem Statement: Write a program function that returns
#  the sum of a list of given numbers
#
#
#  Overall Plan:
#  1.   Print an initial welcoming message to the screen
#  2.   Request numbers list from user either via input and convert to numbers.
#  3.   Pass the input list into a new function to do the math
#  4.	Loop through each number and subsequently add it to a sum variable
#  5.	Take the sum of the array and return it
#  6.   Pass the sum back to the main function and print as the output
#
#  import the necessary python libraries
#  for this example none are needed
	
def sumList(nums):
	# create global variable for main function to print
	global theSum 
	# set sum initial value to 0
	theSum = 0
	
	# loop through each int in list
	for i in nums:
		# add the values in list together as they are looped through
		theSum = theSum + i
		
	# return the sum of the list
	return str(theSum)
	
def main():
	# recieve list of numbers input by the user and convert string to numbers
	print("\nPlease input all of the numbers you'd like")
	nums = eval(input("the sum of separated by a comma (,): \n"))
	
	# evoke the sumList function with the new user-defined parameters
	sumList(nums)
	#print the global theSum variable that was returned from the sumList function
	print(theSum, "is the sum of the list of numbers.\n")
	
main()
		