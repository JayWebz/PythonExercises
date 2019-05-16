#! /usr/bin/python
# Exercise No.   1
# File Name:     hw11project1.py
# Programmer:    Jon Weber
# Date:          Nov. 12, 2017
#
# Problem Statement: Create a program that counts the 
# reserved words in a Python file. 
#
# Overall Plan:
# 1. Identify reserved words file and load into array
# 2. Open python file to check for reserved words
# 3. Print Reserve word count to screen and itemized list
#
# import the necessary python libraries
# None are required

def greet():
	# Greet user and initiate program
	print("This program is a Python Reserved Word Counter")
	print("It will count the number of reserved words in a Python program.")
	input("\n Press <ENTER> to begin.")

def reserveWords():
	# Read list of words from external list file
	infile = open("reserveList.txt", "r")
	# Initialize word list
	reserveWordsList = []
	# split text file based on spacing and add each word to list
	for line in infile:
		word = line.split()
		reserveWordsList = reserveWordsList + word
	# Close word list file and return
	infile.close()
	return reserveWordsList

def checkFile(wordList):
	# Request file to check word list against
	infileName = input("What is the name of the Python file to count?\n")
	# Open file 
	infile = open(infileName, "r")
	# Initialize reserved word count
	reserveCount = 0
	# Initialize tracking for each reserved word that occurs in string
	matches = ""
	# Run through each line in file
	for line in infile:
		# Split up each line
		fileContent = line.split()
		# Run through each word in line
		for word in fileContent:
			# Split up each word
			lineContent = word.split()
			# If any word in wordlist matches word in lineContent
			if any(word in wordList for word in lineContent):
				# Add tally to reserve word count
				reserveCount = reserveCount + 1
				# Add word to matches tracking string
				matches = matches + word + " "
	# Initialize list for counting instances of each word
	wordCountList = []
	# for each word in matches string
	for word in matches.split():
		# Count each instance of each word
		wordCount = matches.count(word)
		# Concatenate word with # of instances of word
		wordCountItem = word, "-", str(wordCount)
		# Join concatenation into single string
		wordCountStr = ''.join(wordCountItem)
		# Add word and word count to list if it has not been yet
		if wordCountStr not in wordCountList:
			wordCountList.append(wordCountStr)
	# Print output of how many reserve words there are
	print("\nThere are", reserveCount, "reserved words")
	print("in this file itemized below:\n")
	# Print which words showed up and how many times they did
	for i in wordCountList:
		print(i)
	print("\n")
	# Close scanned file
	infile.close()

def main():
	# Run introduction function
	greet()
	# Run function to collect word list to check against
	wordList = reserveWords()
	# Run function to check file against word list
	checkFile(wordList)

if __name__ == '__main__':
	main()