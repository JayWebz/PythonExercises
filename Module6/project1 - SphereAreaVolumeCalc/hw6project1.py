#! /usr/bin/python
# Exercise No.   1
# File Name:     hw6project1.py
# Programmer:    Jon Weber
# Date:          Oct. 1, 2017
#
# Problem Statement: Create a multi-function program that outputs the surface
# area and volume of a sphere given the radius 
#
# Overall Plan:
# 1. Create fumction that will calculate the area of a sphere given a radius
# 2. Create a function that will calculate the volume of a sphere given a radius
# 3. Greet the user and introduce the program in a main function
# 4. Prompt user for radius to calculate surface area and radius for volume
# 5. Call functions created in step 1 and 2 with new radius input
# 6. Output surface area and volume data distinguishing between the two
#
# import the necessary python libraries
import math

def sphereArea(radius):
	# spherical surface area = 4pi*r^2
	pi = (math.pi)
	x = 4*pi
	y = radius**2
	surfaceArea = x*y
	return str(surfaceArea)

def sphereVolume(radius):
	# spherical volume = 4/3pi*r^3
	x = (4/3)*(math.pi)
	y = radius**3
	volume = x*y
	return str(volume)

def main():
	# print greeting 
	print("\nHello")
	print("This program will tell you the surface area")
	print("and volume of a sphere when given the radius.\n")

	print("Let's begin")

	# prompt user for radius
	radius = eval(input("Input the radius of the sphere: "))
	
	# evoke sphereArea and sphereVolume functions using radius input
	surfaceArea = sphereArea(radius)
	volume = sphereVolume(radius)

	# print the results of the radius processed through both functions
	print("\nThe surface area is", surfaceArea, "units.")
	print("The volume is", volume, "units.\n")

main()
