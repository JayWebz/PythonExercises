#! /usr/bin/python
#	Exercise No.	3
# 	File Name: 		midtermProject3.py
#	Programmer:		Jon Weber
#	Date: 			October 15, 2017
#
#	Problem Statement: 	Create a program that allows you to 
#	create a connect-the-dot picture. 
#
#
#	Overall Plan:
#
#	1.	Greet User and create GUI interface
#	2.	Prompt User for coordinate points via mouse click that
#		display and number  as they populate
#	3.	Request user to decide if they want to continue plotting or draw
#		after each new point
#	4.	When user is ready, connect the dots between each point in 
#		numerical order. If user hits coord point limit, draw to screen.
#
#
# import the necessary python libraries
from graphics import *

# Define global Coordinate list to collect points
global coordList
coordList = []

def plotPoint(win, pointNum):
	# Get mouse click
	p = win.getMouse()
	# Draw point on screen
	p.draw(win)
	# Number the points as they are drawn
	count = Text(p, pointNum).draw(win)
	count.move(0.5, 0.5)
	coordList.append(p)

def drawLine(win):
	# Set the first coordinate point to position 0 in coordList array.
	coordPoint = 0
	# Determine how many coordinates points there are to connect and try to connect
	for point in range(len(coordList)):
		try:
			# Connect the dots and add one to coordPoint to move on to next point
			Line(coordList[coordPoint], coordList[coordPoint + 1]).draw(win)
			coordPoint = coordPoint + 1
		# Connect the last coordinate point to the first coordinate point 
		except:
			Line(coordList[coordPoint], coordList[0]).draw(win)

def interface():
	#Create GUI window and set window coordinates
	win = GraphWin("Connect the Dots", 960, 720)
	win.setCoords(0, 0, 96, 72)
	#Draw directions seperate from space to plot picture
	rect = Rectangle(Point(-1,7), Point(97, 6)).draw(win)
	rect.setFill(color_rgb(119, 204, 163))
	rect.setOutline(color_rgb(48, 150, 101))
	# Define directions for user
	Text(Point(48, 4.5), "Directions:").draw(win)
	Text(Point(48, 3), "Click on screen to create a new point. You can plot up to 100 points.").draw(win)
	Text(Point(48, 1.5), "After adding a point, let program know if you'd like to continue to plot. When you're done, the dots will connect.").draw(win)
	# Define first point text to appear
	pointNum = 1
	# For points to plot from 1 - 100:
	for p in range(1, 101):
		# Call plot point function to draw on screen
		plotPoint(win, pointNum)
		# Add one to plot point text value
		pointNum = pointNum + 1
		# Check if user wants to plot another point
		if input("\nYou plotted a new point! If you're done plotting, type 'fin',\n or press <ENTER> to continue. ") == "fin":
			# If not, then break from plotting operation and draw line
			drawLine(win)
			break
		# If user hits maximum plot points, stop plotting and draw line
		if pointNum == 101:
			print("\nMaximum points plotted, drawing line...")
			drawLine(win)
			break
			
def main():
	# Greet user and call interface function
	print("\n Let's connect the dots! Choose up to")
	print("100 dots on the interface. When you're done, ")
	print("the line will be drawn connecting them.\n")
	input("Press <ENTER> to continue")
	interface()
	# Reinforce positive plotting habits and end program
	print("\nIt's beautiful! I could see this hanging in a dentist office.\n")
	input("Press <ENTER> to close program")

main()

	
