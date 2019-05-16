#! /usr/bin/python
# Exercise No.   1
# File Name:     finalProject1.py
# Programmer:    Jon Weber
# Date:          Dec. 14, 2017
#
# Problem Statement: Create a program that spell checks
# one file with a provided word file to check against
# and returns words that do not match words in the word file
#
# Overall Plan:
# 1. Create GUI and request inputs from user
# 2. Open dictionary file and read contents to memory
# 3. Open file to spell check and save contents to memory
# 4. Use binary search to see if words from file match dictionary words
# 5. Print words that do not match the words in the dictionary file 
#
# import the necessary python libraries
from graphics import *
from button import Button
import ast

def spellChkGUI():
	# Print window for intro info
	win = GraphWin("Spell Checker 3000", 600, 400)
	win.setBackground("white")
	header = Text(Point(300,30), "Spell Checker 3000")
	header.setSize(24)
	header.setFill("black")
	header.setStyle("bold")
	header.draw(win)
	inputLabel1 = Text(Point(150,100), "File to Check: ").draw(win)
	inputLabel2 = Text(Point(150,170), "Dictionary: ").draw(win)
	inputLabel1.setSize(20)
	inputLabel2.setSize(20)
	inFileNameInput = Entry(Point(450,100), 15).draw(win)
	dictFileNameInput = Entry(Point(450,170), 15).draw(win)
	
	# Create buttons and activate
	spellCheck = Button(win, Point(200, 360), 120, 40, "SPELL CHECK")
	exit = Button(win, Point(400, 360), 120, 40, "EXIT")
	spellCheck.activate()
	exit.activate()
	
	# Look for where user clicks button
	pt = win.getMouse()
	while not exit.clicked(pt):
		if spellCheck.clicked(pt):
			# Return file names if user clicks 'spell check'
			inFileName = inFileNameInput.getText()
			dictFileName = dictFileNameInput.getText()
			spellCheck.deactivate()
			return (inFileName, dictFileName)
		pt = win.getMouse()
	if exit.clicked(pt):
		sys.exit()

def dictionary(dictFile):
	try:
		# Read list of words from external list file
		infile = open(dictFile, "r")
		# Initialize word list
		dictList = []
		# split text file based on spacing and add each word to list
		for line in infile:
			word = line.split()	
			dictList = dictList + word	
		# Close word list file and return
		infile.close()
		return (dictList)
	except:
		print("Please restart the program and enter a valid file to check words against.")
		sys.exit()
	
def getFile(infileName):
	try:
		# Open file 
		infile = open(infileName, "r")
		infileWordsFormatted = []
		# Run through each line in file
		for line in infile:
			# Split up each line
			fileContent = line.split()
			# Run through each word in line
			for word in fileContent:
				# Split up each word
				lineContent = word.split()
				infileWordsFormatted = infileWordsFormatted + lineContent
		# Format infileWordsFormatted by removing special char and spacing
		infileWordsStr = ""
		for word in infileWordsFormatted:
			word = str(word)
			word = word.lower()
			wordOrd = []
			for ch in word:
				numCh = ord(ch)
				if 97 > numCh or 122 < numCh:
					del numCh
				else:
					wordOrd.append(numCh)
			word = ""
			# Convert back to word after stripping excess char
			for num in wordOrd:
				ch = chr(num)
				word = word + ch
			# Add all words to string
			infileWordsStr = infileWordsStr + word + " "
		# Break string up into list
		infileWords = infileWordsStr.split()		
		# Close scanned file and return result
		infile.close()
		return infileWords
	except:
		print("Please restart the program and enter a valid file to spell check.")
		sys.exit()
	
def binary(infileWords, wordList):
	spelledRight = []
	spelledWrong = []
	for word in infileWords:
		low, high = 0, len(wordList) - 1
		correct = False
		while low <= high:				# There is still a range to search
			mid = (low + high) // 2		# Position the middle item
			if wordList[mid] == word:	# Found it! Return the index
				correct = True
				break
			elif wordList[mid] < word:	# x is in lower half of range
				low = mid + 1			#	move top marker down
			else: 						# x is in upper half of range
				high = mid - 1			# 	move bottom marker up
		if correct:
			spelledRight.append(word)
		else:
			spelledWrong.append(word)
	return spelledWrong
	
def main():
	# Create GUI, collect file names
	files = spellChkGUI()
	# Format filenames
	infileName = files[0]
	dictFileName = files[1]
	# Collect words from Dictionary file
	wordList = dictionary(dictFileName)
	# Collect words from file to check
	infileWords = getFile(infileName)
	# Compare words in file list to words in dict list
	spelledWrong = binary(infileWords, wordList)
	# Print words that appear in file list but not in dict list
	print("\nThe following words appear in the checked file and do not match any\ngiven words in the dictionary file, potentially being spelled wrong: \n")
	for i in spelledWrong:
		print(i)
	print()

if __name__ == '__main__':
	main()