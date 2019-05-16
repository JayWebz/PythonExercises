#!   /usr/bin/python
#  Exercise No.   Extra Credit
#  File Name:     hw6extraCredit.py
#  Programmer: 	  Jon Weber
#  Date: 		  Oct. 1, 2017
#
#  Problem Statement: Write a program function that draws a circle to the screen
#  based on where a user clicks. Allow the user to click ten times with the 
#  circle re-centering on each click
#
#  Overall Plan:
#  1.   Greet the user and prompt for GUI to display
#  2.   Request first click from user and draw out a circle. 
#  3.	Re-center the circle nine times based on where the user clicks 
#  4.   After tenth click, allow user to close the GUI
#
#  import the necessary python libraries
from graphics import *

#Define window space for interaction
def drawGrid():
	#Make win accessible in main function
	global win
	#Define window and return
	win = GraphWin("Circle Simulator", 320, 240)
	win.setBackground("white")
	win.setCoords(0, 0, 32, 24)
	return win
	
#Define moveTo function	
def moveTo(circ, p):
	#Find center of circle displayed
    c = circ.getCenter()
    #Recenter x axis
    dx = p.getX() - c.getX()
    #Recenter y axis
    dy = p.getY() - c.getY()
    #move circle to new center
    circ.move(dx,dy)
	
def main():
	#Greet the user
	print("Greetings!")
	print("Let's draw some circles")
	#Prompt to create window
	input("Press <ENTER> to begin")
	drawGrid()

	#Get first mouse click
	p= win.getMouse()
	#Plot Circle centered on mouse click with radius 2
	circ = Circle(Point(p.getX(), p.getY()), 2)
	circ.draw(win)
	#get 2nd Mouse click and redraw
	p2 = win.getMouse()
	moveTo(circ, p2)
	#get 3rd mouse click and redraw, etc.
	p3 = win.getMouse()
	moveTo(circ, p3)
	p4 = win.getMouse()
	moveTo(circ, p4)
	p5 = win.getMouse()
	moveTo(circ, p5)
	p6 = win.getMouse()
	moveTo(circ, p6)
	p7 = win.getMouse()
	moveTo(circ, p7)
	p8 = win.getMouse()
	moveTo(circ, p8)
	p9 = win.getMouse()
	moveTo(circ, p9)
	p10 = win.getMouse()
	moveTo(circ, p10)

	#prompt user to close program
	input("Press <ENTER> to close")
	win.close()
	
main()
	
