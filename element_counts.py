"""
Assignment 4:- 
Create a function that accepts single list containing letters or may be words. Total number of
elements in a list may vary. In turn, it counts the number of occurrences in a list for each
element and returns user a dictionary with total number of counts for each element. Please
remember to include case-sensitive match i.e. 'user1' is not equal to 'User1' word.

Lets say, user provides a list as:
['python', 'pyhton3', 'user1', 'assignment', 'user', 'user1', 'python', 'User1']
Your function should return:
{
	"python": 2,
	"pyhton3": 1,
	"user1": 2,
	"assignment": 1,
	"user": 1,
	"User1":1
}
"""


def CountFrequency(word_list):

    # Creating an empty dictionary
    count = {}
    for word in word_list:

        # Check already exist, If then it will increment the count of specific word
        count[word] = count.get(word, 0) + 1
    print('{}'.format(count))


# Predefine word list
word_list = ['python', 'pyhton3', 'user1',
             'assignment', 'user', 'user1', 'python', 'User1']
CountFrequency(word_list)  # Calling function to count frequency of each word
