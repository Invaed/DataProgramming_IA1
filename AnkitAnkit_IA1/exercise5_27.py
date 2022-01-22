#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# Write a program that displays the π value for i = 10000 , 20000 , …, and 100000 .
#############################################
denominator = 1
sum = 0
for pi in range(10000, 100001, 10000):
    for i in range(1000):
        if i % 2 == 0:
            sum += 4 / denominator
        else:
            sum -= 4 / denominator
        denominator += 2
    print("pi value for", pi, "is:", sum)