#!   /usr/bin/python
#  Exercise No.   3
#  File Name:     hw7project3.py
#  Programmer: 	  Jon Weber
#  Date: 		  Oct. 8, 2017
#
#  Problem Statement: Write a program function that returns
#  how much to charge for a speeding ticket based on speed of offender
#
#
#  Overall Plan:
#  1. Greet User and prompt for speed and speed limit in mph
#  2. Determine if speed is within legal limit
#  3. Determine if speed is over 90 for extra base fee
#  4. If speed is over legal limit, determine variable rate to charge
#  5. Output rate to charge
#
#  import the necessary python libraries
#  for this example none are needed

def main():
	#Greet user and request inputs
	print("\nThis program will calculate speeding ticket fines for Poducksville.")
	print("\nLet's begin:")
	limit = eval(input("\nWhat is the speed limit in mph? "))
	speed = eval(input("How fast was the offender going in mph? "))

	#Set base fee rate to 50 dollars
	baseRate = 50
	#Set base fee to 250 dollars if offender went faster than 90mph
	if speed >= 90:
		baseRate = 250

	#Determine if offender broke the law
	if speed < limit:
		print("\nSpeed is within legal limits.")
	
	#Determine variable rate charged for each mph over the legal limit
	elif speed > limit:
		#Multiply mph over limit by 5 dollars
		varRate = (speed - limit) * 5
		#Add variable rate to base rate and print result
		rate = baseRate + varRate
		print("\nThe offender is to be charged $", rate, sep="")
main()
		