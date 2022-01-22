#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Financial application: payroll) Write a program that reads the following information and
# prints a payroll statement:
# Employee’s name (e.g., Smith)
# Number of hours worked in a week (e.g., 10)
# Hourly pay rate (e.g., 9.75)
# Federal tax withholding rate (e.g., 20%)
# State tax withholding rate (e.g., 9%)
#############################################
employee_name = input("Enter employee name: ")
no_of_hrs_worked_in_week = int(input("Enter no of hours worked in a week: "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))
federal_tax_withholding_rate = float(input("Enter federal tx withholding rate: "))
state_tax_withholding_rate = float(input("Enter state tax withholding rate: "))
weekly_gross_pay = (hourly_pay_rate * no_of_hrs_worked_in_week)
payroll_statement = weekly_gross_pay - (weekly_gross_pay * (federal_tax_withholding_rate/100)) - (weekly_gross_pay * (state_tax_withholding_rate/100))
print("payroll statement:", payroll_statement)