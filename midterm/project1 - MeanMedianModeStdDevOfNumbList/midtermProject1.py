#!   /usr/bin/python
#  Exercise No.   1
#  File Name:     midtermProject1.py
#  Programmer: 	  Jon Weber
#  Date: 		  Oct. 15, 2017
#
#   Problem Statement: Write a program that finds the mean, median,
#	and standard deviation of a list numbers read from a file.
#	# One number per line and should support negative and positive numbers 
#
#
#	Overall Plan:
#	1. Greet user and request filename with file parameters
#	2. Determine if file content are within defined parameters 
#	2. Read list and populate contents into array
#	3. Sort array from smallest to largest
#	4. Determine Mean
#	5. Determine Median
#	6. Determine Standard Deviation Ranges
#	7. Return values to user
#
#  import the necessary python libraries

import math

def main():
	#Greet user
	print("\nThis program will calculate the mean, median, and standard deviation")
	print("of a file that contains a list of numbers with one number per line.\n")
	print("Let's Begin:\n")

	# Select file name to open and to save to
	infileInput = input("What is the name of the file to pull data from? ")
	infileName = open(infileInput, "r")
	
	# See if the input file only contains numbers
	try:
		# Read file and populate into an array
		data = []
		for string in infileName: 	
			num = string.split()	
			data = data + num
	
	# Check if there is only one number per line:
		# Count how many lines are in the file
		fileLineCount = sum(1 for line in open(infileInput))
		# Count how many items are in the array
		dataLen = len(data)
		
		# Verify that lines in file and items in array are equal to each other
		if fileLineCount == dataLen:
		# Continue with calculations
			# Sort array from smallest to largest and convert from string to float
			data.sort(key=float)
			
			# Print array to user
			print("Here is the data that will be used: \n", data)
			input("\nPress <ENTER> to continue")
		
			# Find mean of list
			dataSum = sum(float(i) for i in data)
			mean = dataSum / dataLen
		
			# Find median of list
			center = dataLen / 2
			# If there is no absolute center, find
			# difference between two center numbers
			if dataLen % 2 == 0:
				#Define lower end of center point
				centerLow = (dataLen // 2) - 1
				# Define upper end of center point
				centerHigh = centerLow + 1
				# Find the difference between the two center points
				centerPoint = float(data[centerLow]) + float(data[centerHigh])
				median = centerPoint / 2
			# Otherwise print middle number in list	
			else:
				center = dataLen // 2
				median = (data[center])
			
			# Find the Standard Deviation of list
			sdNumArray = []
			for num in data:
				# Standard Deviation = sqrt(sum( X - M )^2 / (n - 1))
				# Solve for (X - M)^2
				valueLessMean = float(num) - mean
				valueLessMeanSq = valueLessMean**2
				# Solve for (n - 1)
				sampleSizeLessOne = dataLen - 1
				# Solve for ( X - M )^2 / (n - 1)
				sdNumSum = valueLessMeanSq / sampleSizeLessOne
				# Compile results into array
				sdNumSum = [float(sdNumSum)]
				sdNumArray = sdNumArray + sdNumSum
		
			# Find sum of standard deviation array
			sdArraySum = sum(sdNumArray)
			# Find Square Root of Sum
			sd = math.sqrt(sdArraySum)
			# Find range of standard deviation
			meanLessSd = mean - sd
			meanPlusSd = mean + sd
			# Print Results
			print("\nData Set Mean: ", mean)
			print("Data Set Median: ", median)
			print("Standard Deviation Range:", meanLessSd, "to", meanPlusSd, "\n")
		else:
			print("\nPlease ensure your data file only has one number per line")
			print("and that there are no extra spaces in your file.\n")
		
		# Close the data file
		infileName.close()
	# If file contains more char types than floats or ints, return statement.
	except ValueError:
		print("The data set needs to only contain numbers.")
	
main()		