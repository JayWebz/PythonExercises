#! /usr/bin/python
# Exercise No.   3
# File Name:     hw4project3.py
# Programmer:    Jon Weber
# Date:          Sept. 17, 2017
#
# Problem Statement: Create a program that allows the user to
# draw a line segment and then display graphical and textual 
# information about the line segment.
#
# Overall Plan:
# 1. Create a window for objects and print welcome message to window
# 2. Request the user make two mouse clicks to depict the line segment
# 3. Have user verify coordinate points and prompt for calculations
# 4. Determine the midpoint of the line segment
# 5. Determine the slope of the line segment
# 6. Draw the line with midpoint in cyan.
# 7. Print the length and slope of the line to screen
# 8. Close window when prompted by the user
#
# import the necessary python libraries
import graphics
from graphics import *
import math
from math import * 

def main():
	# Open white graphics window
	win = graphics.GraphWin("Line Segment Tool", 300, 400)
	win.setBackground("white")

	# Set coordinates to go from (0,0) lower left to (3,4) in upper right
	win.setCoords(0.0, 0.0, 3.0, 4.0)

	# Print a message to the window and display grid
	Text(Point(1.5, 3.875), "Hello!").draw(win)
	Text(Point(1.5, 3.75), "Click two points on the 3x3 grid below to make a line.").draw(win)
	Text(Point(1.5, 3.625), "I will return the line's midpoint, length, and slope.").draw(win)
	xAxis = Rectangle(Point(0.05,0.05), Point(2.95,0.1))
	yAxis = Rectangle(Point(0.05,0.05), Point(0.1,2.95))
	xAxis.setFill(color_rgb(0,182,182))
	yAxis.setFill(color_rgb(0,182,182))
	xAxis.setOutline(color_rgb(0,182,182))
	yAxis.setOutline(color_rgb(0,182,182))
	xAxis.draw(win)
	yAxis.draw(win)

	# Store user input click data
	p1 = win.getMouse()
	p1.draw(win)
	p2 = win.getMouse()
	p2.draw(win)

	# Have user verify click data coordinates and prompt for calculation
	Text(Point(0.5, 3.375), "Point 1: ").draw(win)
	outputP1X = Text(Point(1, 3.375), " ").draw(win)
	outputP1Y = Text(Point(1.25, 3.375), " ").draw(win)
	Text(Point(0.5, 3.25), "Point 2: ").draw(win)
	outputP2X = Text(Point(1, 3.25), " ").draw(win)
	outputP2Y = Text(Point(1.25, 3.25), " ").draw(win)
	button = Text(Point(2.25, 3.3125), "Find The Slope").draw(win)
	Rectangle(Point(1.75, 3.1925), Point (2.75, 3.435)).draw(win)
	outputP1X.setText("%.2f" % p1.getX())
	outputP2X.setText("%.2f" % p2.getX())
	outputP1Y.setText("%.2f" % p1.getY())
	outputP2Y.setText("%.2f" % p2.getY())

	# Wait for mouse click
	win.getMouse()

	# Determine Midpoint of line segment and draw to screen
	xAvg = (p1.getX() + p2.getX()) / 2
	yAvg = (p1.getY() + p2.getY()) / 2
	midpoint = Point(xAvg, yAvg)
	midpointDot = Circle(midpoint, 0.05)
	midpointDot.setFill(color_rgb(0,255,255))
	midpointDot.setOutline(color_rgb(0,255,255))

	# Draw the line and midpoint
	Line(p1, p2).draw(win)
	midpointDot.draw(win)

	# Calculate the length
	dx = p2.getX() - p1.getX()
	dy = p2.getY() - p1.getY()
	xLength = (dx)**2
	yLength = (dy)**2
	lineLength = math.sqrt(xLength + yLength)

	# Calculate the slope
	slope = dy / dx

	# Print length of line and slope to screen
	Text(Point(0.5, 3.125), "Length: ").draw(win)
	outputLength = Text(Point(1.175, 3.125), " ").draw(win)
	outputLength.setText("%.2f" % lineLength)
	Text(Point(0.5, 3), "Slope: ").draw(win)
	outputSlope = Text(Point(1.175, 3), " ").draw(win)
	outputSlope.setText("%.2f" % slope)

	# Output the results and change button
	button.setText("Quit")

	# Wait for click and then quit
	win.getMouse()
	win.close()

main()
