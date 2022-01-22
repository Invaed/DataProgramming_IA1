#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Financial application: calculate tips) Write a program that reads the subtotal and the
# gratuity rate and computes the gratuity and total. For example, if the user enters 10
# for the subtotal and 15% for the gratuity rate, the program displays 1.5 as the
# gratuity and 11.5 as the total.
#############################################
subtotal = float(input("Enter subtotal value: "))
gratuity_rate = float(input("Enter gratuity rate value: "))
gratuity = gratuity_rate/subtotal
total = subtotal + gratuity
print("gratuity:", gratuity)
print("total:", total)