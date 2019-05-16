#!   /usr/bin/python
#  Exercise No.   2
#  File Name:     hw10project2.py
#  Programmer: 	  Jon Weber
#  Date: 		  Nov. 5, 2017
#
#
#	Graphics program to roll a pair of dice. Uses custom widgets
#	Button and DieView

from random import randrange
from graphics import GraphWin, Point

from cbutton import cButton
from dieview import DieView

def main():
	# Create the application window
	win = GraphWin("Dice Roller")
	win.setCoords(0, 0, 10, 10)
	win.setBackground("green2")
	
	# Draw the interface widgets
	die1 = DieView(win, Point(3,7), 2)
	die2 = DieView(win, Point(7,7), 2)
	rollButton = cButton(win, Point(1.5,3), 2.5, "Roll Dice")
	rollButton.activate()
	quitButton = cButton(win, Point(6,3), 2.5, "Quit")
	
	# Event Loop
	pt = win.getMouse()
	while not quitButton.clicked(pt):
		if rollButton.clicked(pt):
			value1 = randrange(1,7)
			die1.setValue(value1)
			value2 = randrange(1,7)
			die2.setValue(value2)
			quitButton.activate()
		pt = win.getMouse()
	
	# Close up shop
	win.close()

main()