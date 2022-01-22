#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Check a number) Write a program that prompts the user to enter an integer and checks
# whether the number is divisible by both 5 and 6 , divisible by 5 or 6 , or just one of
# them (but not both).
#############################################
number = int(input("Enter an integer number: "))
if number%5==0 and number%6==0:
    print(number,"is divisible by both 5 and 6")
elif number%5==0 or number%6==0:
    print(number,"is divisible by 5 or 6 but not both")
else:
    print(number,"is divisible by neither 5 or 6")