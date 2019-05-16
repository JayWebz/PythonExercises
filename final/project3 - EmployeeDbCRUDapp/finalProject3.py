#! /usr/bin/python
# Exercise No.   3
# File Name:     finalProject3.py
# Programmer:    Jon Weber
# Date:          Dec. 14, 2017
#
# Problem Statement: Provide a management system to manage
# employees in a database. Be able to add delete employees,
# view employee records, and calculate pay for each employee.
#
# Overall Plan:
# 1. Request user info for records file
# 2. Open records and store employee record in dictionary
# 3. Have menu for user to specify how to interact with employee objects 
# with each menu item as a different task
# 4. When user is done managing files, have option to save data to new file 
#
# import the necessary python libraries
from emp import Employee
import sys

def createEmployee(records):
	# Gather inputs to create employee object
	firstName = input("Employee first name: ")
	lastName = input("Employee last name: ")
	employeeID = input("Employee ID Number: ")
	status = input("Employment status (pt, ft, hourly): ")
	payRate = input("Pay Rate (ft in annual terms, pt in rate per class, hourly in rate per hour): ")
	# Create employee record and set key for dictionary storage
	emp = Employee(firstName, lastName, employeeID, status, payRate)
	empRec = emp.addRecord(firstName, lastName, employeeID, status, payRate)
	records[employeeID] = empRec
	print("\n Employee Record Added.")
	return records
	
def delEmployee(records):
	try:
		# Retrieve employee information
		employeeID = input("What is the ID number of the employee? ")
		record = records.get(employeeID)
		# Generate employee
		firstName, lastName, employeeID, status, payRate = record[0], record[1], record[2], record[3], record[4]
		emp = Employee(firstName, lastName, employeeID, status, payRate)
		# Verify employee info
		verifyDelStr = "Are you sure you want to delete " + firstName + " " + lastName + ", ID: " + employeeID + ", from records (y/n)?"
		verifyDel = input(verifyDelStr)
		# If yes, remove employee record
		if verifyDel[0] in "Yy":
			del records[employeeID]
			print("Record Deleted.")	
	except:
		print("Error: Please enter a valid employee ID.")

def getEmployeeInfo(records):
	try:
		# Retrieve employee information
		employeeID = input("What is the ID number of the employee? ")
		record = records.get(employeeID)
		# Generate employee
		firstName, lastName, employeeID, status, payRate = record[0], record[1], record[2], record[3], record[4]
		emp = Employee(firstName, lastName, employeeID, status, payRate)
		# Request employee info
		empInfo = emp.employeeInfo(firstName, lastName, employeeID, status, payRate)
		# Return employee info
		print(empInfo)
	except:
		print("Error: Please enter a valid employee ID.")
	
def getPayRate(records):
	try:
		# Retrieve employee information
		employeeID = input("What is the ID number of the employee? ")
		record = records.get(employeeID)
		# Generate employee
		firstName, lastName, employeeID, status, payRate = record[0], record[1], record[2], record[3], record[4]
		emp = Employee(firstName, lastName, employeeID, status, payRate)
		# Calculate Gross Pay
		grossPay = emp.calculatePay(status, payRate)
		# Return Gross Pay info dependent on employment status
		if status == "ft":
			print("$", grossPay, " per month, at $", payRate, " per year.", sep="")
		elif status == "pt":
			print("$", grossPay, ", at $", payRate, " per class.", sep="")
		elif status == "hourly":
			print("$", grossPay, ", at $", payRate, " per hour.", sep="")
	except:
		print("Error: Please enter a valid employee ID.")
	
def saveRecords(records):
	# Write all records to record file with new name provided by user
	recordFile = input("What records file should be saved to? ")
	file = open(recordFile, "w")
	recordValues = records.values()
	# Cycle through printing each record on a line with items seperated with spaces
	for value in recordValues:
		for i in value:
			file.write(i + " ")
		file.write("\n")
	file.close()
	print("File Saved.")
	
def openRecords():
	try:
		# Initialize records dictionary, request records file to use
		records = {}
		recordFile = input("What records file should be opened? ")
		# Read file contents
		with open(recordFile) as file:
			recordsCount = 0
			for line in file:
				recordsCount = recordsCount + 1
		#for record in records:
		for line in open(recordFile, "r"):	
			# Extract record from file
			firstName, lastName, employeeID, status, payRate = line.split()
			record = [firstName, lastName, employeeID, status, payRate] 
			# Store record in dictionary with employeeID as key, close file
			for i in range(recordsCount):
				records[employeeID] = record
			file.close()
		print("File Opened.")
		return records
	except:
		print("Please restart the program and enter a valid record file.")
		sys.exit()

def menu(records):	
	# Request user action	
	userAction = input("\nWhat would you like to do?\nPlease Select:\n\n(1) Create New Employee\n(2) Delete Existing Employee\n(3) View Employee Info\n(4) Calculate Pay\n(q) Quit Program\n")
	while True:
		if userAction == '1':
			# Create new employee
			createEmployee(records)
			# Return to menu
			menu(records)
		elif userAction == '2':
			# Delete existing employee
			delEmployee(records)
			# Return to menu
			menu(records)
		elif userAction == '3':
			# View current employee information
			getEmployeeInfo(records)
			# Return to menu
			menu(records)
		elif userAction == '4':
			#Calculate pay
			getPayRate(records)
			# Return to menu
			menu(records)
		elif userAction == 'q':
			# Ask to save changes and close program
			saveChanges = input("Do you want to save changes? ")
			if saveChanges[0] in "yY":
				saveRecords(records)
				sys.exit()
			else:
				print("Exiting Program without saving.")
				sys.exit()
	
def main():
	# Open record file upon startup
	records = openRecords()		
	# Print intro and provide menu
	print("\nWelcome to the School Management System.")
	menu(records)					

if __name__ == '__main__':
	main()