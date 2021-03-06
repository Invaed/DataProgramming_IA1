#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Geometry: area of a regular polygon) A regular polygon is an n-sided polygon in which all
# sides are of the same length and all angles have the same degree (i.e., the polygon is
# both equilateral and equiangular). The formula for computing the area of a regular
# polygon is
# area = (n x (s)^2) / 4 x tan(pi/n)
# Here, s is the length of a side. Write a program that prompts the user to enter the
# number of sides and their length of a regular polygon and displays its area.
#############################################
import math
n = int(input("Enter the number of sides: "))
s = int(input("Enter the length of sides: "))
area = (n * (s**2)) / (4 * math.tan(math.pi/n))
print("Area of polygon:", area)