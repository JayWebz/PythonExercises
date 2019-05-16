class Employee:
	"""employee is an object that creates and manipulates data about a particular employee such as calculating pay, printing employee info, ."""
	
	# Initialize attributes
	def __init__(self, firstName, lastName, employeeID, status, payRate):
		self.firstName = firstName
		self.lastName = lastName
		self.employeeID = employeeID
		self.status = status
		self.payRate = payRate
	
	# Create record list provided employee info
	def addRecord(self, firstName, lastName, employeeID, status, payRate):
		record = [self.firstName, self.lastName, self.employeeID, self.status, self.payRate]
		return record
	
	# Calculate employee pay	
	def calculatePay(self, status, payRate):
		# Full Time
		if self.status == 'ft':
			self.payRate = float(self.payRate)
			grossPay = self.payRate / 12
			return grossPay
		# Part Time
		elif self.status == 'pt':
			self.payRate = float(self.payRate)
			classCount = input("How many classes were taught? ")
			classCount = float(classCount)
			grossPay = self.payRate * float(classCount)
			return grossPay
		# Hourly
		elif self.status == 'hourly':
			self.payRate = float(self.payRate)
			hourCount = input("How many hours were worked? ")
			grossPay = self.payRate * float(hourCount)
			return grossPay
	
	# Print current data on employee
	def employeeInfo(self, firstName, lastName, employeeID, status, payRate):
		return "Employee {} {}, id number {}, is {} status, at a rate of ${}.".format(self.firstName, self.lastName, self.employeeID, self.status, self.payRate)