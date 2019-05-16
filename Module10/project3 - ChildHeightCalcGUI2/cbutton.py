# button.py
from graphics import *
from math import *

class cButton:
	
	""""A button is a labeled rectangle in a window.
	It is activated or deactivated with the activate()
	and deactivate() methods. The clicked(p) method
	returns true if the button is active and p is inside it."""
	
	def __init__(self, win, center, radius, label):
		""" Creates a circular button, eg:
		qb = Button(myWin, centerPoint, radius, 'Quit') """
		r = radius/2.0
		self.r = r
		x,y = center.getX(), center.getY()
		self.x, self.y = x+r, y+r
		p = Point(self.x, self.y)
		self.circ = Circle(p, r)
		self.circ.setFill('lightgray')
		self.circ.draw(win)
		self.label = Text(p, label)
		self.label.draw(win)
		self.deactivate()

	def clicked(self, p):
		"Returns true if button active and p is inside"
		dx = p.getX() - self.x
		dy = p.getY() - self.y
		dist = sqrt(dx*dx + dy*dy)
		
		return (self.active and
		dist <= self.r)
# 		self.x <= p.getX() and
# 		self.y <=p.getY())

	def getLabel(self):
		"Returns the label string of this button."
		return self.label.getText()

	def activate(self):
		"Sets button to 'active'."
		self.label.setFill('black')
		self.active = True

	def deactivate(self):
		"Sets button to 'inactive'."
		self.label.setFill('darkgrey')
		self.active = False