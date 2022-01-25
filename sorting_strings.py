"""
Assignment 2:-
Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again

Then, the output should be:
again and hello makes perfect practice world
"""


def Quicksort(word_list):
    # This function returns string assorted.
    if not word_list:
        return []
    sorted_string = (Quicksort([x for x in word_list[1:] if x < word_list[0]])
            + [word_list[0]] +
            Quicksort([x for x in word_list[1:] if x >= word_list[0]]))
    return sorted_string


def RemoveDuplicates(lst):
    # This function will remove duplicate words from list.
    word_list = []
    for word in lst:
        if word not in word_list:
            word_list.append(word)
        else:
            continue
    return word_list


# User input and calling predefin functions
supplied_input = input("Please enter a string: ")
supplied_input_splited = supplied_input.split(' ')

word_list = RemoveDuplicates(supplied_input_splited)
sorted_string = Quicksort(word_list)
print((' ').join(sorted_string))
