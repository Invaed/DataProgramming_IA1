#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Financial application: investment amount) Suppose you want to deposit a certain
# amount of money into a savings account with a fixed annual interest rate. Write a
# program that prompts the user to enter the final account value, the annual interest rate
# in percent, and the number of years, and then displays the initial deposit amount. The
# initial deposit amount can be obtained using the following formula:
# initialDepositAmount = finalAccountValue / ((1 + monthlyInterestRate)^numberOfMonths))
#############################################
finalAccountValue = float(input("Enter final account value: "))
annualInterestRate = float(input("Enter annual interest rate in percentage: "))
numberOfYears = float(input("Enter the number of years: "))
initialDepositAmount = finalAccountValue/(1 + ((annualInterestRate/12)**(numberOfYears*12)))
print("Initial Deposit Amount:", initialDepositAmount)