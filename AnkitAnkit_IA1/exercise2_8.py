#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Science: calculate energy) Write a program that calculates the energy needed to heat
# water from an initial temperature to a final temperature. Your program should prompt
# the user to enter the amount of water in kilograms and the initial and final
# temperatures of the water. The formula to compute the energy is as follows:
# Q = M * (finalTemperature - initialTemperature) * 4184
# where M is the weight of water in kilograms, temperatures are in degrees Celsius, and
# energy Q is measured in joules.
#############################################
M = float(input("Enter the amount of water in kilograms: "))
initialTemperature = float(input("Enter the initial temperature of water: "))
finalTemperature = float(input("Enter the final temperature of water: "))
Q = M * (finalTemperature - initialTemperature) * 4184
print("Energy required:", Q, "joules")
