#! /usr/bin/python
# Exercise No.   1
# File Name:     hw4project1.py
# Programmer:    Jon Weber
# Date:          Sept. 17, 2017
#
# Problem Statement: Draw a simple picture with at least 3 graphical objects. 
#
# Overall Plan:
# 1. Create a window for objects with a simple grid
# 2. Map out, fill, and draw a rectangle to screen
# 3. Map out, fill, and draw a triangle to screen layered over the rectangle
# 4. Map out, fill, and draw a circle to a corner of the window
# 5. Clone the circle 3 times and move to each quadrant
# 6. Have the visible window close when prompted by the user
#
# import the necessary python libraries
import graphics
from graphics import *

def main():
	# Open white graphics window
	win = graphics.GraphWin("Shapes", 300, 300)
	win.setBackground("white")

	# Set coordinates to go from (0,0) lower left to (2,2) in upper right
	win.setCoords(0.0, 0.0, 2.0, 2.0)

	# Define the points of a rectangle, color, and draw to screen
	rect = Rectangle(Point(0.165, 0.165), Point(1.835, 1.835))
	rect.setFill(color_rgb(172,125,125))
	rect.setOutline(color_rgb(102,52,52))
	rect.draw(win)

	#Define the points of a triangle, color, and then draw to screen
	tp1 = Point(1, 1.67)
	tp2 = Point(0.33, 0.33)
	tp3 = Point(1.67, 0.33)
	triangle = Polygon(tp1, tp2, tp3)
	triangle.setFill(color_rgb(100,132,100))
	triangle.setOutline(color_rgb(41,82,41))
	triangle.draw(win)

	# Draw a cyan circle in the ll quadrant
	centQuadrant = Point(0.5, 0.5)
	circll = Circle(centQuadrant, 0.45)
	circll.setFill(color_rgb(0,255,255))
	circll.setOutline(color_rgb(0,182,182))
	circll.draw(win)

	#clone circle and move to lr quadrant, change color to yellow
	circlr = circll.clone()
	circlr.move(1,0)
	circlr.setFill(color_rgb(255,255,0))
	circlr.setOutline(color_rgb(182,182,0))
	circlr.draw(win)

	#clone circle and move to ur quadrant, change color to magenta
	circur = circlr.clone()
	circur.move(0,1)
	circur.setFill(color_rgb(255,0,255))
	circur.setOutline(color_rgb(182,0,182))
	circur.draw(win)

	#clone ll circle and move to ul quadrant, change color to black/white
	circul = circll.clone()
	circul.move(0,1)
	circul.setFill(color_rgb(255,255,255))
	circul.setOutline(color_rgb(0,0,0))
	circul.draw(win)

	input("Press <enter> to quit.")
	win.close()

main()
