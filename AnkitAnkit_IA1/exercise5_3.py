#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Conversion from kilograms to pounds) Write a program that displays the following table
# (note that 1 kilogram is 2.2 pounds):
#############################################
print("Kilograms\tPounds")
for i in range(1, 200, 2):
    print(i, "\t\t", str(round(i*2.2, 2)).rjust(10))