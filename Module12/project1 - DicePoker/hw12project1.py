#! /usr/bin/python
# Exercise No.   1
# File Name:     hw12project1.py
# Programmer:    Jon Weber
# Date:          Nov. 19, 2017
#
# Problem Statement: Create an app to play dice poker.
# Include high scores record, help menu, and splash screen
#
# Overall Plan:
# 1. Print splash screen that displays rules and high scores
# 2. If player decides to play game, display main game interface with dice
# 3. Allow player to roll dice three times or score round as is. 
# 4. Keep a record of current money in game, starting at $100.
# 5. If user scores in the top ten, record score to display on splash screen. 
#
# import the necessary python libraries
from button import Button
from pokerapp import PokerApp
from dieview import DieView
from graphics import *
from sys import *
from pokerGUI import GraphicsInterface
import ast
# help screen and high scores record code kept in pokerGUI.py

def intro():
	# Print window for intro info
	win = GraphWin("Dice Poker", 600, 400)
	win.setBackground("green3")
	header = Text(Point(300,30), "Python Poker Parlor")
	header.setSize(24)
	header.setFill("yellow2")
	header.setStyle("bold")
	header.draw(win)
	rule1 = Text(Point(300,60), "To begin, select `LET'S PLAY` below.").draw(win)
	rule2 = Text(Point(300,85), "Each round begins by selecting `ROLL DICE`.").draw(win)
	rule3 = Text(Point(300,110), "A round costs $10 to play. You begin with $100.").draw(win)
	rule4 = Text(Point(300,135), "Select a Die button to identify which to reroll. Red dice get rerolled.").draw(win)
	rule5 = Text(Point(300,160), "Reroll die up to two times. If you do not wish to reroll, select `SCORE`").draw(win)
	rule6 = Text(Point(300,185), "Decide to press your luck or cash out from the table.").draw(win)
	# Cycle through rules and set uniform styling
	rules = [rule1, rule2, rule3, rule4, rule5, rule6]
	for i in range(6):
		rules[i].setSize(15)
	# High Scores Listing
	scores = Text(Point(300,215), "High Scores")
	scores.setSize(24)
	scores.setFill("yellow2")
	scores.setStyle("bold")
	scores.draw(win)
	# Read high score values to print to window
	topScoresFile = open("scores.txt", "r")
	topScoresList = topScoresFile.read()
	topScores = []
	for score in topScoresList.split("\n"):
		topScores.append(score)

	rank = ["1ST: ", "2ND: ", "3RD: ", "4TH: ", "5TH: ", "6TH: ", "7TH: ", "8TH: ", "9TH: ", "10TH: "]
	p1 = Text(Point(200,240), rank[0] + topScores[9]).draw(win)
	p2 = Text(Point(200,260), rank[1] + topScores[8]).draw(win)
	p3 = Text(Point(200,280), rank[2] + topScores[7]).draw(win)
	p4 = Text(Point(200,300), rank[3] + topScores[6]).draw(win)
	p5 = Text(Point(200,320), rank[4] + topScores[5]).draw(win)
	p6 = Text(Point(400,240), rank[5] + topScores[4]).draw(win)
	p7 = Text(Point(400,260), rank[6] + topScores[3]).draw(win)
	p8 = Text(Point(400,280), rank[7] + topScores[2]).draw(win)
	p9 = Text(Point(400,300), rank[8] + topScores[1]).draw(win)
	p10 = Text(Point(400,320), rank[9] + topScores[0]).draw(win)
	del topScores[10:]
	topScoresFile.close()
	# Create buttons and activate
	play = Button(win, Point(200, 360), 120, 40, "LET'S PLAY")
	exit = Button(win, Point(400, 360), 120, 40, "EXIT")
	play.activate()
	exit.activate()
	# Look for where user clicks button
	pt = win.getMouse()
	while not exit.clicked(pt):
		if play.clicked(pt):
			win.close()
			return
		pt = win.getMouse()
	if exit.clicked(pt):
		sys.exit()

def main():
	intro()
	# Build and execute app
	inter = GraphicsInterface()
	app = PokerApp(inter)
	app.run()
main()