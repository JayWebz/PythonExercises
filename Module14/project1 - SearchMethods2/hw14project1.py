#! /usr/bin/python
# Exercise No.   1
# File Name:     hw14project1.py
# Programmer:    Jon Weber
# Date:          Dec. 3, 2017
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
def standardSort(nums):
	nums.sort()

def selectionSort(nums):
	n = len(nums)
	# For each position in the list (except the very last)
	for bottom in range(n - 1):
		# Find the smallest items in num[bottom]..nums[n-1]
		mp = bottom						# Bottom is smallest initially
		for i in range(bottom + 1, n):	# Look at each position
			if nums[i] < nums[mp]:		# This one is smaller
				mp = i					# 	Remember it's index
		# Swap smallest item to the bottom
		nums[bottom], nums[mp] = nums[mp], nums[bottom]

def merge(lst1, lst2, lst3):
	# Merge sorted lists lst1 and lst2 into lst3

	# These indexes keep track of current position in each list
	i1, i2, i3 = 0, 0, 0			# All start at the front
	n1, n2 = len(lst1), len(lst2)

	# Loop while both lst1 and lst2 have more items
	while i1 < n1 and i2 < n2:
		if lst1[i1] < lst2[i2]:	# Top of lst1 is smaller
			lst3[i3] = lst1[i1]	# Copy it into current spot in lst3
			i1 = i1 + 1
		else:					# Top of lst2 is smaller
			lst3[i3] = lst2[i2]	# Copy it into current spot in lst3
			i2 = i2 + 1
		i3 = i3 + 1				# Item added to lst3, update position

	#	Here either lst1 or lst2 is done. One of the following loops will
	#	execute to finish up the merge.

	# Copy remaining items (if any) from lst1
	while i1 < n1:
		lst3[i3] = lst1[i1]
		i1 = i1 + 1
		i3 = i3 + 1
	# Copy remaining items (if any) from lst2
	while i2 < n2:
		lst3[i3] = lst2[i2]
		i2 = i2 + 1
		i3 = i3 + 1

def mergeSort(nums):
	# Put items of nums in ascending order
	n = len(nums)
	# Do nothing if list contains 0 or 1 items
	if n > 1:
		# Split into two sublists
		m = n // 2
		nums1, nums2 = nums[:m], nums[m:]
		# Recursively sort each piece
		mergeSort(nums1)
		mergeSort(nums2)
		# Merge the sorted pieces back into original list
		merge(nums1, nums2, nums)

def main():
	# Collect inputs from user, item to search for, where to search, how to search
	infileName = input("What file should be sorted?\n")
	searchType = input("How should the item be searched, Select: \n  '1' for Standard Sort\n  '2' for Selection Sort\n  '3' for Merge Sort.\n")
	# Append file contents to array nums
	nums = []
	openInfile = open(infileName, "r")
	fileContents = openInfile.read()
	# Start processing clock
	start_time = time.time()
	# Process based on user choice
	for num in fileContents:
		nums.append(num)
	
	# Process sort type selected for list
	if searchType[0] == '1':
		standardSort(nums)

	elif searchType[0] == '2':
		selectionSort(nums)

	elif searchType[0] == '3':
		mergeSort(nums)
	
	else: 
		print("Please select a valid value to indicate sort type.")

	print("This computation took %s seconds to process" % (time.time() - start_time))
main()

"""Verify the sort results. Compare the sort times of python standard sort, 
selection sort and merge sort for the list sizes of 5000, 50000, and 500000.   
Put the results in a file called hw14project1.txt and put the code 
in a file called hw14project1.py """