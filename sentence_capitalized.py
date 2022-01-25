"""
Assignment 1:-
Write a program that accepts multiple number of sentences as input and prints the lines after
making all characters in the sentence capitalized.

Ex:- Suppose the following input is supplied to the program:
Hello world
Practice makes perfect

Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""


def Uppercase(supplied_string):
    for i in range(0, len(supplied_string)):

        x = ord(supplied_string[i])  # Check ASCII value of each char
        if x >= 97 and x <= 122:
            x = x-32  # Convert into lower case
        y = chr(x)
        print(y, end="")


supplied_string = input("Enter the string to be converted uppercase: ")
Uppercase(supplied_string)  # Call method to convert string into uppercase
