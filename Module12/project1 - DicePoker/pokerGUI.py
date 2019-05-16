#textpoker
from button import Button
from pokerapp import PokerApp
from dieview import DieView
from graphics import *

class GraphicsInterface:
	def __init__(self):
		self.win = GraphWin("Dice Poker", 600, 400)
		self.win.setBackground("green3")
		banner = Text(Point(300,30), "Python Poker Parlor")
		banner.setSize(24)
		banner.setFill("yellow2")
		banner.setStyle("bold")
		banner.draw(self.win)
		self.msg = Text(Point(300,380), "Welcome to the Dice Table")
		self.msg.setSize(18)
		self.msg.draw(self.win)
		self.createDice(Point(300,100), 75)
		self.buttons = []
		self.addDiceButtons(Point(300,170), 75, 30)
		b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
		self.buttons.append(b)
		b = Button(self.win, Point(300, 280), 150, 40, "Score")
		self.buttons.append(b)
		b = Button(self.win, Point(570,375), 40, 30, "Quit")
		self.buttons.append(b)
		b = Button(self.win, Point(30,375), 40, 30, "Help")
		self.buttons.append(b)
		self.money = Text(Point(300, 325), "$100")
		self.money.setSize(18)
		self.money.draw(self.win)

	def createDice(self, center, size):
		center.move(-3 * size, 0)
		self.dice = []
		for i in range(5):
			view = DieView(self.win, center, size)
			self.dice.append(view)
			center.move(1.5 * size, 0)

	def addDiceButtons(self, center, width, height):
		center.move(-3 * width, 0)
		for i in range(1,6):
			label = "Die {0}".format(i)
			b = Button(self.win, center, width, height, label)
			self.buttons.append(b)
			center.move(1.5 * width, 0)

	def choose(self, choices):
		buttons = self.buttons
		# Activate choice buttons, deactivate others
		for b in buttons:
			if b.getLabel() in choices:
				b.activate()
			else:
				b.deactivate()
		# Get mouse clicks until an active button is clicked while True:
		while True:
			p = self.win.getMouse()
			for b in buttons:
				if b.clicked(p):
					return b.getLabel() # Function exit here

	def setMoney(self, amt):
		self.money.setText("${0}".format(amt))

	def showResult(self, msg, score):
		if score > 0:
			text = "{0}! You win ${1}".format(msg, score)
		else: 
			text = "You rolled {0}".format(msg)
		self.msg.setText(text)

	def setDice(self, values):
		for i in range(5):
			self.dice[i].setValue(values[i])

	def wantToPlay(self):
		ans = self.choose(["Roll Dice", "Quit"])
		self.msg.setText("")
		return ans == "Roll Dice"

	def chooseDice(self):
		# choices is a list of the indexes of the selected dice
		choices = []	# No dice chosen yet
		while True:
			# Wait for user to click a valid button
			b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5", 
							"Roll Dice", "Score", "Help"])
			if b[0] == "D":			# User clicked a die button
				i = eval(b[4]) - 1	# Translate label to die index
				if i in choices:	# Currently selected, unselect it
					choices.remove(i)
					self.dice[i].setColor("black")
				else:				# Currently unselected, select it
					choices.append(i)
					self.dice[i].setColor("red")
			else: 					# User clicked roll or score
				for d in self.dice:	# Revert appearance of all dice
					d.setColor("black")
				if b == "Score":	# Score clicked, ignore choices
					return []
				elif b == "Help":	# Help clicked, popup window
					helpWin = GraphWin("Dice Poker Help", 360, 400)
					helpWin.setBackground("green3")
					# Create Help Header
					header = Text(Point(180,30), "Rules")
					header.setSize(24)
					header.setFill("yellow2")
					header.setStyle("bold")
					header.draw(helpWin)
					# Display rules to window
					rule2 = Text(Point(180,60), "Select `ROLL DICE` to begin.").draw(helpWin)
					rule3 = Text(Point(180,80), "A round costs $10 to play. You begin with $100.").draw(helpWin)
					rule4 = Text(Point(180,100), "Select a Die to reroll. Red dice get rerolled.").draw(helpWin)
					rule5 = Text(Point(180,120), "Reroll die up to two times. Select `SCORE` if no reroll desired").draw(helpWin)
					rule6 = Text(Point(180,140), "Decide to press your luck or cash out from the table.").draw(helpWin)
					rule7 = Text(Point(180,160), "Top high scores are recorded.").draw(helpWin)
					# Display payouts to window
					payout = Text(Point(180,190), "Payouts")
					payout.setSize(24)
					payout.setFill("yellow2")
					payout.setStyle("bold")
					payout.draw(helpWin)
					payouts = ["5", "8", "12", "15", "20", "30"]
					payout1 = Text(Point(180,220), "Two Pair: $" + payouts[0]).draw(helpWin)
					payout2 = Text(Point(180,240), "Three of Kind: $" + payouts[1]).draw(helpWin)
					payout3 = Text(Point(180,260), "Full House: $" + payouts[2]).draw(helpWin)
					payout4 = Text(Point(180,280), "Four of Kind: $" + payouts[3]).draw(helpWin)
					payout5 = Text(Point(180,300), "Straight: $" + payouts[4]).draw(helpWin)
					payout6 = Text(Point(180,320), "Five of Kind: $" + payouts[5]).draw(helpWin)
					exit = Button(helpWin, Point(180, 360), 120, 40, "EXIT")
					exit.activate()
					# Look for where user clicks button
					pt = helpWin.getMouse()
					while not exit.clicked(pt):
						pt = helpWin.getMouse()
					if exit.clicked(pt):
						helpWin.close()

				elif choices != []:	# Don't accept Roll unless some
					return choices	# dice are actually selected

	def close(self):
		# Get player score
		scoreStr = str(self.money)
		char1 = "$"
		char2 = '"'
		userScore = scoreStr[scoreStr.find(char1) + 1 : scoreStr.find(char2) - 1]
		# Open high score file to check against
		file = open("scores.txt", "r")
		message = file.read()
		scores = []
		users = []
		for score in message.split("\n"):
			users.append(score[0:3])
			scores.append(score[4:])
		# If user score is greater than lowest stored score
		intLowestScore = float(scores[0])
		intUserScore = float(userScore)
		if intLowestScore < intUserScore:
			# Prompt for User Initials
			scoreWin = GraphWin("Dice Poker New High Score", 360, 140)
			scoreWin.setBackground("green3")
			header = Text(Point(180,30), "Enter Three Initials")
			header.setSize(24)
			header.setFill("yellow2")
			header.setStyle("bold")
			header.draw(scoreWin)
			userInitialInput = Entry(Point(180,60), 4).draw(scoreWin)
			enter = Button(scoreWin, Point(180,100), 120, 40, "ENTER")
			enter.activate()
			# Look for where user clicks button
			pt = scoreWin.getMouse()
			while not enter.clicked(pt):
				pt = scoreWin.getMouse()
			if enter.clicked(pt):
				scoreWin.close()
			# Add user Initials and score to list and remove lowest
			del scores[0]
			del users[0]
			scores.append(userScore)
			userInitial = userInitialInput.getText()
			# Strip spaces out of input name
			userInitial = userInitial.replace(" ", "")
			userInitial = userInitial.upper()
			users.append(userInitial[0:3])
			# Combine score and user arrays
			topScores = scores + users
			# Check for blank list items first, remove if present
			topScores = [i for i in topScores if len(i)!=0]
			# Link score and username back together
			for i in range(10):
				topScores[i] = topScores[i + 10] + " " + topScores[i]
			del topScores[10:]
			# Sort list with new high score
			topScores = sorted(topScores, key = lambda x: float(x.split(' ')[1]))
			# Save high scores to file, close file
			file.close()
			scoreFile = open("scores.txt", "w")
			for item in topScores:
				print(item, file=scoreFile)
			scoreFile.close()
		# Close program
		self.win.close()