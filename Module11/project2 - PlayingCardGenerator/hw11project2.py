#! /usr/bin/python
# Exercise No.   2
# File Name:     hw11project2.py
# Programmer:    Jon Weber
# Date:          Nov. 12, 2017
#
# Problem Statement: Create a program that will
# input the suit and value of a card and output 
# a picture of the corresponding card.
#
# Overall Plan:
# 1. Create GUI with text box, button, and picture
# 2. Request suit and value to display from user
# 3. Output picture of suit.
#
# import the necessary python libraries
from graphics import *
from button import Button

def guiContent(win):
	# Greet user and prompt for inputs
	Text(Point(5,9.5), "This program will print a picture of a playing card").draw(win)
	Text(Point(5,9), "based on user input. Let's begin:").draw(win)		
	Text(Point(4.5,8.25), "Select: 'spades', 'hearts', 'clubs', or 'diamonds':").draw(win)
	Text(Point(5.2,7.5), "Select a card value: 2-10, J, Q, K, A: ").draw(win)
	
	# Draw card frame to display
	rect = Rectangle(Point(3, 2), Point(7, 7))
	rect.setFill("white")
	rect.setOutline(color_rgb(102,52,52))
	rect.draw(win)

def main():
	# Create Application Window
	win = GraphWin("Card Generator", 400, 400)
	win.setCoords(0, 0, 10, 10)
	win.setBackground("white")
	# Draw objects to window
	guiContent(win)
	# Create input boxes for values
	suit = Entry(Point(8.5,8.25), 9).draw(win)
	card = Entry(Point(8.5,7.5), 9).draw(win)
	
	# Draw buttons to screen, activate submit button
	submit = Button(win, Point(3,1), 2, 1, "Submit")
	submit.activate()
	quit = Button(win, Point(7,1), 2, 1, "Quit")

	# Allow user to provide inputs and wait for click
	pt = win.getMouse()
	
	# While user did not click the 'quit' button
	while not quit.clicked(pt):
		# If the user clicked the 'submit' button
		if submit.clicked(pt):
			# Translate suit input into string and append .gif file extension
			suitImageFile = suit.getText() + '.gif'
			# Translate card value input and change to uppercase
			cardValue = card.getText()
			cardValue = cardValue.upper()
			# Draw a rectangle to clear out prior card value inputs
			valueClear = Rectangle(Point(3.2,6.5), Point(3.6,6.8)).draw(win)
			valueClear.setFill("white")
			valueClear.setOutline("white")
			# Check for valid inputs and execute if they are
			try:
				# Draw suit image to screen
				img = Image(Point(5,4.5), suitImageFile).draw(win)
				# Change card value to print to red if heart or diamond
				if suitImageFile == "hearts.gif" or suitImageFile == "diamonds.gif":
					# Draw card value to this location and set color to red
					value = Text(Point(3.4,6.6), cardValue)
					value.setFill("red")
					# Check if valid card value, if so draw to screen
					if cardValue in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
						value.draw(win)
					# If not valid card value, display error
					else: 
						Text(Point(5,1.75), "Please restart the program and input a valid card value.").draw(win)
						submit.deactivate()
				# If spade or club, draw card value to screen
				else: 
					value = Text(Point(3.4,6.6), cardValue).draw(win)
			# If inputs not valid, display error
			except:
				Text(Point(5,1.75), "Please restart the program and input a valid suit.").draw(win)
				submit.deactivate()
			# Activate quit button after one loop
			quit.activate()
		# Determine where user clicks and repeat loop if not 'quit' button
		pt = win.getMouse()
	# Close the program if 'quit' button
	win.close()
	#run the proper formula given gender input. If invalid gender, return message

if __name__ == '__main__':
	main()
