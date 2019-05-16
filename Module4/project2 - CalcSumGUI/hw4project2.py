#! /usr/bin/python
# Exercise No.   2
# File Name:     hw4project2.py
# Programmer:    Jon Weber
# Date:          Sept. 17, 2017
#
# Problem Statement: Create a Graphical User Interface
# for a program that calculates sum and product of three numbers.
#
# Overall Plan:
# 1. Create a window for objects and print welcome message to window
# 2. Create input field for integers to be used in calculations
# 3. Calculate the sum of the integers
# 4. Calculate product of integers
# 5. Print the sum of the integers on screen with label
# 6. Print the product of the integers to screen with label
# 7. Close window when prompted by the user
#
# import the necessary python libraries
import graphics
from graphics import *

def main():
	# Open white graphics window
	win = graphics.GraphWin("Sum and Product Finder", 300, 300)
	win.setBackground("white")

	# Set coordinates to go from (0,0) lower left to (3,3) in upper right
	win.setCoords(0.0, 0.0, 3.0, 3.0)

	# Print a message to the window
	Text(Point(1.5,2.75), "Hello!").draw(win)
	Text(Point(1.5,2.5), "I can add and multiply three numbers for you").draw(win)

	# Create input fields for integers used in calculations below 
	Text(Point(1,2), "Enter first number: ").draw(win)
	num1input = Entry(Point(2,2), 5).draw(win)
	Text(Point(1,1.75), "Enter second number: ").draw(win)
	num2input = Entry(Point(2,1.75), 5).draw(win)
	Text(Point(1,1.5), "Enter third number: ").draw(win)
	num3input = Entry(Point(2,1.5), 5).draw(win)

	#Create output fields and content
	Text(Point(1, 1), "Sum: ").draw(win)
	outputSum = Text(Point(2, 1), " ").draw(win)
	Text(Point(1, 0.75), "Product: ").draw(win)
	outputProduct = Text(Point(2, 0.75), " ").draw(win)
	button = Text(Point(1.5, 0.25), "Do the math").draw(win)
	Rectangle(Point(1.125, 0.125), Point (1.875, 0.375)).draw(win)

	#wait for mouse click
	win.getMouse()

	# Convert the inputs into integers
	num1 = eval(num1input.getText())
	num2 = eval(num2input.getText())
	num3 = eval(num3input.getText())

	# Calculate values of sum and product of three numbers
	sum = num1 + num2 + num3
	product = num1 * num2 * num3

	# Output the results and change button
	outputSum.setText(sum)
	outputProduct.setText(product)
	button.setText("Quit")

	# Wait for click and then quit
	win.getMouse()
	win.close()

main()
