# Employee Name

employeeName = input("Please enter the employee name: ")

# Transaction Dollar Value

transactionValue = float(input("Please input the employees total dollar transaction value: "))

# Number of Transactions

numOfTransactions = int(input("Please input the number of transactions: "))

# Number of Shifts

numOfShifts = int(input("Please input the number of shifts worked: "))

# Calculate Productivity Score

productivityScore = (transactionValue/numOfTransactions)/numOfShifts

# Nested if-statements
if productivityScore <= 30:
  employeeBonus = 50.00 
elif productivityScore > 31 or productivityScore < 69:
  employeeBonus = 75.00
elif productivityScore > 70 or productivityScore < 199:
  employeeBonus = 100.00
elif productivityScore >= 200:
  employeeBonus = 200.00