#! /usr/bin/python
# Exercise No.   1
# File Name:     hw13project1.py
# Programmer:    Jon Weber
# Date:          Nov. 26, 2017
#
# Problem Statement: Verify the search results. 
# Compare the search times of linear search and 
# binary search for the list sizes of 1000, 10000, and 100000. 
#
# Overall Plan:
# 1. Create binary search and linear search algorithms.
# 2. Request list size from user to process search time for. 
#
# import the necessary python libraries
import time

def linear(x, nums):
	for i in range(len(nums)):		
		if nums[i] == x:			# Item found, return the index value
			return i
	return -1						# Loop finished, item was not in list

def binary(x, nums):
	low = 0
	high = len(nums) - 1
	while low <= high:				# There is still a range to search
		mid = (low + high) // 2		# Position the middle item
		item = nums[mid]
		if x == item:				# Found it! Return the index
			return mid
		elif x < item:				# x is in lower half of range
			high = mid - 1			#	move top marker down
		else: 						# x is in upper half of range
			low = mid + 1			# 	move bottom marker up
	return -1						# No range left to search, x is not there

def main():
	# Collect inputs from user, item to search for, where to search, how to search
	infileName = input("What file should be searched?\n")
	x = input("What should be searched for?\n")
	searchType = input("How should the item be searched, 'linear' or 'binary'?\n")
	# Start processing clock
	start_time = time.time()
	# Append file contents to array nums
	nums = []
	openInfile = open(infileName, "r")
	fileContents = openInfile.read()
	for num in fileContents:
		nums.append(num)
	# Process search type selected for list
	if searchType[0] == 'L' or searchType[0] == 'l':
		linear(x, nums)

	elif searchType[0] == 'B' or searchType[0] == 'b':
		nums.sort()
		binary(x, nums)
	else: 
		print("Please select a valid search type.")
	print("This computation took %s seconds to process" % (time.time() - start_time))
main()

