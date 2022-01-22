#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Financial: compare costs) Suppose you shop for rice and find it in two different-sized
# packages. You would like to write a program to compare the cost of the packages. The
# program prompts the user to enter the weight and price of each package and then
# displays the one with the better price.
#############################################
weight_pck1 = float(input("Enter weight of package 1: "))
price_pck1 = float(input("Enter price of package 1: "))
weight_pck2 = float(input("Enter weight of package 2: "))
price_pck2 = float(input("Enter price of package 2: "))

if weight_pck1/price_pck1 > weight_pck2/price_pck2:
    print("Package 1 has better price")
else:
    print("Package 2 has better price")