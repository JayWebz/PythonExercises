#! /usr/bin/python
# Exercise No.   1
# File Name:     hw5project1.py
# Programmer:    Jon Weber
# Date:          Sept. 24, 2017
#
# Problem Statement: Create a program that allows the user to type in 
# a phrase and then outputs the acronym for that phrase. 
#
# Overall Plan:
# 1. Collect Phrase to turn into acronym from user in single input
# 2. Split the input into string methods based on word spacing
# 3. Loop through each string and collect the first letter
# 4. Join the letters from indexing each word and collecting position 0 together
# 5. Capitalize the characters
# 6. Output the answer
#
# import the necessary python libraries
# none necessary

def main():
	
	# Print title
	print("Thudpucker's Acronym Generator")

	# Collect phrase from user via input
	phraseStr = input("Please enter the phrase to be converted into an acronym: ")
	
	# Create a blank character-holding list
	chars = []

	# Loop through each word of the phrase input by user
	for wordStr in phraseStr.split():
		# Append the first letter of each word to the chars list
		chars.append(wordStr[0])

	# Create acronym string by combining all the substrings stored in char list.
	acronym = "".join(chars)

	# Capitalize acronym and print to screen
	print("Your chosen acronym is:", acronym.upper())

main()
