#! /usr/bin/python
# Exercise No.   2
# File Name:     hw13project2.py
# Programmer:    Jon Weber
# Date:          Nov. 26, 2017
#
# Problem Statement: Create a program using  
# a recursive function that can detect
# if a given string is a palindrome. 
#
# Overall Plan:
# 1. Request input string from user
# 2. Load input into array, strip special characters, casing, and spacing
# 3. Determine if first and last letter are the same.
# 4. Determine if string in between is identical reading backwards and forwards
# 5. Output result of palindrome test
#
# import the necessary python libraries
import ast

def palindrome(s):
	if s == "":
		# got to end of string, matches palindrome check
		print("It's a palindrome :D ")
		return s
	# if first ch is same as last ch:
	elif s[0] == s[len(s) - 1]: 
		# remove first and last ch
		sEnd = len(s) -1
		s = s[1:sEnd]
		# re-run palindrome test until string is empty	
		palindrome(s)
		return s
	# if a char does not match the letter matching it reading backwards:
	else:
		print("Not a palindrome :( ")

def main():
	s = input("input string to test if palindrome:\n")
	# remove casing
	s = s.lower()
	# remove special char or spacing from s via unicode
	sOrd = []
	for ch in s:
		numCh = ord(ch)
		if 97 > numCh or 122 < numCh:
			del numCh
		else:
			sOrd.append(numCh)
	s = ""
	# convert back to char
	for num in sOrd:
		ch = chr(num)
		s = s + ch
 	# execute palindrome check with processed string s
	palindrome(s)
main()