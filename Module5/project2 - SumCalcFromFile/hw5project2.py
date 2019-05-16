#!   /usr/bin/python
#  Exercise No.   2
#  File Name:     hw5project2.py
#  Programmer: Jon Weber
#  Date: Sept. 24, 2017
#
#  Problem Statement: Write a program that opens a file 
#  and reads each line into a list. Process each item by converting
#  the two number strings into a list of numbers and summing them together.
#
#
#  Overall Plan:
#  1.   Print an initial welcoming message to the screen
#  2.   Prompt the user for a file name of integers to add together
#  3.   convert the two number strings in each line into integers
#  4.   Add the integers together per each line
#  5.   Write the sum out to a file, output.txt
#
#
#  import the necessary python libraries
#  for this example none are needed

def main():
	# Introduce the program
	print("This program will take a text file of numbers listed out")
	print("and sum them together per each new line in the text file")
	input("Press <ENTER> to continue")
	
	# Select file name and open it
	infileName = open("input.txt", "r")
	outfileName = open("output.txt", "w")
	
	# process each line of the file
	for line in infileName:
		# Get the strings from each line
		str1, str2 = line.split()
		# Convert the the strings into numbers
		num1 = eval(str1)
		num2 = eval(str2)
		# Add the values together
		sum = num1 + num2
		# Write to output file
		print(sum, file=outfileName)
		
	# Close both files
	infileName.close()
	outfileName.close()
	
	print("The sum of each line from input.txt can be found in output.txt")
	
main()
		