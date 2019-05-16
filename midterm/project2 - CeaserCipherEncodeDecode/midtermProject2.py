#!   /usr/bin/python
#  Exercise No.   2
#  File Name:     midtermProject2.py
#  Programmer: 	  Jon Weber
#  Date: 		  Oct. 15, 2017
#
#   Problem Statement: Write a program to encode and decode
#	Caesar ciphers. A Caesar cipher is a simple substituition
#	cipher where a letter in a message is shifted X positions
#	in the alphabet. i.e. F shifts 2 slots to H; Y shifts to A 
#
#
#	Overall Plan:
#	1. Greet User and request task to complete
#	2. If user wants to encode
#		a.	request filename to decode to
#		b.	read message and convert char to appropriate Unicode
#		c.	Convert numbers to characters with cipher applied
#		d.	Output cipher string to new file
#	3.	If user wants to decode
#		a.	Request filename to uncode to
#		b.	Read message and convert char to appropraite Unicode
#		c.	Convert numbers to cahracter with cipher removed
#		d.	Output uncoded string to new file
#
#  import the necessary python libraries
#  for this example none are needed

def main():
	# Introduce the program
	print("\nThis program will encode and decode Caesar ciphers.")
	print("\nLet's begin:")
	input("Press <ENTER> to continue\n")
	# Request task from user
	task = input("Which function needs to be performed? Type 'encode' or 'decode': ")
	
	# Determine which task to undertake based on user input
	if task == "encode":
		# Request filename to encode
		file = input("What is the name of the file to encode? ")
		
		# Select file name and open it, select file to save to when done
		infileName = open(file, "r")
		
		# Get outfileName desired by user
		outputFile = input("What would you like the encoded file to be called? ")
		outfileName = open(outputFile, "w")
		
		# Copy file contents to variable
		message = infileName.read()
		
		# Create empty list to populate char digits
		charCode = []
		for ch in message:
			# Convert characters to digits
			codeNum = (ord(ch))
			# If Unicode number is between a - x, add 2
			if 97 <= codeNum <= 120:
				codeNum = codeNum + 2
			# If Unicode number is between A - X, add 2
			elif 65 <= codeNum <= 88:
				codeNum = codeNum + 2
			#If Unicode number is Y, then A
			elif codeNum == 89:
				codeNum = 65
			# If Unicode number is Z, then B
			elif codeNum == 90:
				codeNum = 66
			# If Unicode number is y, then a
			elif codeNum == 121:
				codeNum = 97
			# If Unicode number is z, then b
			elif codeNum == 122:
				codeNum = 98
			# If Unicode is special not a char, let it be
			else:
				codeNum = codeNum
			# Append Unicode results to list
			charCode.append(codeNum)
		
		# Convert each number to encoded letter and store in empty string
		caeserCode = ""
		for num in charCode:
			caeserCode = caeserCode + chr(num)

		# Print String to output file
		print(caeserCode, file=outfileName)
		
		# Close both files
		infileName.close()
		outfileName.close()
		
		# Notify user program has completed operation
		print("\nThe encoded message from", file, "can be found in", outputFile)
	
	elif task == "decode":
		# Request filename to encode
		file = input("What is the name of the file to decode? ")
		
		# Select file name and open it, select file to save to when done
		infileName = open(file, "r")
		
		# Get outfileName desired by user
		outputFile = input("What would you like the decoded file to be called? ")
		outfileName = open(outputFile, "w")
		
		# Copy file contents to variable
		message = infileName.read()
		
		# Convert each letter in message into unicode - 2 and put in array
		charCode = []
		for ch in message:
			codeNum = (ord(ch))
			# If Unicode number is between a - x, reduce 2
			if 99 <= codeNum <= 122:
				codeNum = codeNum - 2
			# If Unicode number is between A - X, reduce 2
			elif 67 <= codeNum <= 90:
				codeNum = codeNum - 2
			# If Unicode number is A, then Y
			elif codeNum == 65:
				codeNum = 89
			# If Unicode number is B, then Z
			elif codeNum == 66:
				codeNum = 90
			# If Unicode number is a, then y
			elif codeNum == 97:
				codeNum = 121
			# If Unicode number is b, then z
			elif codeNum == 98:
				codeNum = 122
			# If Unicode is special not a char, let it be
			else:
				codeNum = codeNum
			# Append Unicode results to list
			charCode.append(codeNum)
		
		# Convert each number to decoded letter and store in empty string
		uncodedCode = ""
		for num in charCode:
			uncodedCode = uncodedCode + chr(num)

		# Print String to output file
		print(uncodedCode, file=outfileName)
		
		# Close both files
		infileName.close()
		outfileName.close()
		
		# Notify user program has completed operation
		print("\nThe decoded message from", file, "can be found in", outputFile)
	else:
		print("please select a valid option.")
	
main()
