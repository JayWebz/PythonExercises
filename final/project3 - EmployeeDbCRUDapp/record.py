class Employee:
	"""employee is an object that creates and manipulates data about a particular employee such as calculating pay, printing employee info, ."""
	
	# Initialize attributes
	def __init__(self, firstName, lastName, employeeID, status, payRate):
		self.firstName = firstName
		self.lastName = lastName
		self.employeeID = employeeID
		self.status = status
		self.payRate = payRate
	
	# Calculate employee pay	
	def calculatePay(self, status, payRate):
		if self.status == 'ft':
			self.payRate = float(self.payRate)
			monthlyRate = self.payRate / 12
			print(monthlyRate, "per month")
		elif self.status == 'pt':
			self.payRate = float(self.payRate)
			classCount = input("How many classes were taught? ")
			classCount = float(classCount)
			grossPay = self.payRate * classCount
			print(grossPay, ", at", payRate, "per class")
		elif self.status == 'hourly':
			self.payRate = float(self.payRate)
			hourCount = input("How many hours were worked? ")
			grossPay = self.payRate * hourCount
			print(grossPay, ", at", payRate, "per hour")
	
	# Print current data on employee
	def employeeInfo(self, firstName, lastName, employeeID, status, payRate):
		print("Employee {} {}, id number {}, is {}, at a rate of {}.".format(self.firstName, self.lastName, self.employeeID, self.status, self.payRate))