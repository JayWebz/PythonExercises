#! /usr/bin/python
# Exercise No.   3
# File Name:     hw6project3.py
# Programmer:    Jon Weber
# Date:          Oct. 1, 2017
#
# Problem Statement: Create a multi-function program that prints the lyrics
# for ten verses of "The Ants Go marching." Choose your a different activity 
# for the little one in each verse that will still allow for a rhyme. 
#
# Overall Plan:
# 1. Define functions that output lyrics
# 2. Create a variable to stand in where each part of the lyrics change, numText and rhyme
# 3. Create a stanza function that will evoke the smaller functions that print taking in numText
#    and rhyme as parameters.
# 4. Call stanza ten times in main function, passing through each one the correct numText and rhyme.

# import the necessary python libraries
# none are needed

def marchingHurrah(numText):
	print("The ants go marching ", numText, " by ", numText, ", hurrah! hurrah!", sep='')

def marching(numText):
	print("The ants go marching ", numText, " by ", numText, ",", sep='')

def littleOne(rhyme):
	print("The little one stops", rhyme)

def endVerse():
	print("And they all go marching down...\nIn the ground...")
	print("To get out...\nOf the rain.\nBoom! Boom! Boom!")

def stanza(numText, rhyme):
	marchingHurrah(numText)
	marchingHurrah(numText)
	marching(numText)
	littleOne(rhyme)
	endVerse()

def main():
	stanza('ten', 'to find his zen,')
	print()
	stanza('nine', 'to meet Frankenstein,')
	print()
	stanza('eight', 'because he was deadweight,')
	print()
	stanza('seven', 'for that commie, Lenin,')
	print()
	stanza('six', 'on Route 66')
	print()
	stanza('five', 'and needs to be revived,')
	print()
	stanza('four', 'in Baltimore')
	print()
	stanza('three', 'to put on her skis,')
	print()
	stanza('two', 'to tame a shrew',)
	print()
	stanza('one', 'because she was done,')

main()





