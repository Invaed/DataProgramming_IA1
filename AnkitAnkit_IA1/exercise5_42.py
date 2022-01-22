#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Process string) Write a program that prompts the user to enter a string and displays the
# characters at odd positions.
#############################################
input_string = input("Enter string: ")
odd_string = ""
for i in range(0, len(input_string), 2):
    odd_string = odd_string + input_string[i]

print(odd_string)
