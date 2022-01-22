#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Financials: currency exchange) Write a program that prompts the user to enter the
# currency exchange rate between U.S. dollars and Chinese Renminbi (RMB). Prompt the
# user to enter 0 to convert from U.S. dollars to Chinese RMB and 1 for vice versa. Prompt
# the user to enter the amount in U.S. dollars or Chinese RMB to convert it to Chinese
# RMB or U.S. dollars, respectively.
#############################################
exchange_rate = float(input("Enter currency exchange rate between USD to RMB: "))
option = int(input("""Enter 0 to convert USD to RMB
Enter 1 to convert RMB to USD: """))
amount = float(input("Enter the amount to convert: "))
converted_amount = 0
if option==0:
    converted_amount = amount * exchange_rate
elif option==1:
    converted_amount = amount / exchange_rate
print("Converted amount:", converted_amount)