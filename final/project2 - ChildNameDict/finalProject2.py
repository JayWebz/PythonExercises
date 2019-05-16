#! /usr/bin/python
# Exercise No.   2
# File Name:     finalProject2.py
# Programmer:    Jon Weber
# Date:          Dec. 14, 2017
#
# Problem Statement: Create a program that reads two files into memory
# with names and how often they are used using a dictionary. Allow the 
# user to input a name and return information about it from the files.
#
# Overall Plan:
# 1. Read two files into memory
# 2. Request user input of name to check
# 3. Search both files for name and output rank and count if it's there
# 4. If the name isn't in file, output statemnt saying not there. 
#
# import the necessary python libraries
# None are needed

def main(): 
	#Read name files to memory
	namesBoy = {}
	namesGirl = {}

	for line in open("boynames.txt", "r"):
		name, count = line.split()
		name = name.lower()
		namesBoy[name] = count

	for line in open("girlnames.txt", "r"):
		name, count = line.split()
		name = name.lower()
		namesGirl[name] = count

	# Request name to search for
	print("\nEnter a name and this program will tell you")
	print("if that name is ranked among the top 1000 names")
	print("given in 2003, as well as how many times that")
	print("name was registered in that year.\n")
	search = input("What name should be searched for?\n")
	search = search.lower()

	# Look for name in files
	if search in namesBoy.keys():
		# Get Rank, add 1
		position = list(namesBoy.keys()).index(search) + 1
		# Get Naming Count
		usage = namesBoy[search]
		# Capitalize name for print out
		search = search.title()
		print(search, "is ranked", position, "in popularity among boys with", usage, "namings.")
		print(search, "is not ranked among the top 1000 girl names.")
	elif search in namesGirl.keys():
		# Get Rank, add 1
		position = list(namesGirl.keys()).index(search) + 1
		# Get Naming Count
		usage = namesGirl[search]
		# Capitalize name for print out
		search = search.title()
		print(search, "is ranked", position, "in popularity among girls with", usage, "namings.")
		print(search, "is not ranked among the top 1000 boy names.")
	else:
		# Capitalize name and notify user name is not ranked.
		search = search.title()
		print(search, "is not ranked among the top 1000 boy names.")
		print(search, "is not ranked among the top 1000 girl names.")

if __name__ == '__main__':
	main()