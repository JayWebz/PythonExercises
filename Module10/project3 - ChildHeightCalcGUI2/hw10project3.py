#!   /usr/bin/python
#  Exercise No.   3
#  File Name:     hw10project3.py
#  Programmer: 	  Jon Weber
#  Date: 		  Nov. 5, 2017
#
#  Problem Statement: Write a program function that returns
#  the expected height of a child, based on it's gender and height of parents.
#
#
#  Overall Plan:
#  1. Greet User and prompt for gender 
#  2. Prompt user for height of parents
#  3. Calculate height based on gender input
#  4. Solve formula for child height with given parent height input
#  5. Output expected height of child
#
#  import the necessary python libraries
from graphics import *
from cbutton import cButton

def intro(win):
	#Greet user
	Text(Point(5,9), "This program will calculate the expected height of a child").draw(win)
	Text(Point(5,8.5), "When they become an adult. Let's begin:").draw(win)		
	
def maleChild(win, momHeight, dadHeight):
	#Apply formula to determine expected male height and print result in inches
	hMale = ((momHeight * 13/12) + dadHeight) / 2
	mResults = "The expected height of the son will be ", "%.1f" % hMale, " inches."
	mString = ''.join(mResults)
	Text(Point(5,2), mString).draw(win)

def femaleChild(win, momHeight, dadHeight):
	#Apply formula to determine expected female height and print result in inches
	hFemale = ((dadHeight * 12/13) + momHeight) / 2
	fResults = "The expected height of the daughter will be ", "%.1f" % hFemale, " inches."
	fString = ''.join(fResults)
	Text(Point(5,2), fString).draw(win)

def main():
	
	# Create Application Window
	win = GraphWin("Height Estimator", 400, 400)
	win.setCoords(0, 0, 10, 10)
	win.setBackground("white")
	
	# Run intro
	intro(win)

	# Build inputs
	# Request child gender and height of parents via GUI
	Text(Point(3,7), "Input gender of child as 'm' or 'f'?").draw(win)
	gender = Entry(Point(8,7), 5).draw(win)
	
	Text(Point(3,6), "What is the height of the mother?").draw(win)
	momHeightVal = Entry(Point(8,6), 5).draw(win)
	
	Text(Point(3,5), "What is the height of the father?").draw(win)
	dadHeightVal = Entry(Point(8,5), 5).draw(win)
		
	# Create buttons and activate 'submit' button
	submit = cButton(win, Point(2.5,2.5), 2, "Submit")
	submit.activate()
	quit = cButton(win, Point(5.5,2.5), 2, "Quit")
	
	# Allow user to provide inputs and wait for click
	pt = win.getMouse()
	
	# While user did not click the 'quit' button
	while not quit.clicked(pt):
		# If the user clicked the 'submit' button
		if submit.clicked(pt):
			# Translate inputs into readable nums and chars
			# Try compiling information
			try:
				childGender = gender.getText()
				momHeight = eval(momHeightVal.getText())
				dadHeight = eval(dadHeightVal.getText())
	
				# Run the appropriate function depending on gender input
				if childGender == "m":
					maleChild(win, momHeight, dadHeight)
				elif childGender == "f":
					femaleChild(win, momHeight, dadHeight)
				else:
					print("Please input a valid gender")
			# If missing fields, display error message
			except:
				Text(Point(5,2), "Please fill in all inputs with valid values after restarting the program").draw(win)
			# Activate quit button after one loop
			quit.activate()
			submit.deactivate()
		# Determine where user clicks and repeate loop if not 'quit' button
		pt = win.getMouse()
	# Close the program if 'quit' button
	win.close()
	#run the proper formula given gender input. If invalid gender, return message
	
main()
		