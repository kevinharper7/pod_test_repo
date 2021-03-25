'''
GOOGLING CHALLENGE! 
Today, we'll ask you to write a bunch of small pieces of code.
Unlike previous ones, we have NOT showed you the exact code you'll need to answer the questions.
So, you'll want to search out answers on the web, make sure you understand them, then try them out until they work!
For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE SOLUTION in so that you can use it in the future too
'''


# 1A. Sort the below list in alphabetical order
print('QUESTION 1\n')
my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']
my_friends.sort()
print(my_friends)

# 1B. Comment your code in 1A to convince yourself you understand how it works
# The sort function is a list function that by default sorts elements in order.
print('\n')

# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
print('QUESTION 2\n')

my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}

# 2B. Comment your code in 2A to convince yourself you understand how it works
# Using code to first identify my_account_keys with my_account_keys function.

my_account_keys = my_account.keys()
# Printing out the data keys all at once.
print(my_account_keys)
print('\n')
# Checking the data type of my_account _keys.
print(type(my_account_keys))
print('\n')


# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')

my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'

# 3B. Comment your code in 3A to convince yourself you understand how it works
# Creating a new variable wood_count to count the number of times wood appears in the string.
wood_count = my_string.count('wood')
print(f'The word "wood" appears {wood_count} times in the string provided.')
print('\n')


# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')

my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']

# 4B. Comment your code in 4A to convince yourself you understand how it works
banana_count = my_list.count('banana')
print(f'The word "banana" appears {banana_count} times in the string provided.')
print('\n')



# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
# 5B. Comment your code in 5A to convince yourself you understand how it works
print('QUESTION 5\n')
print(*my_list)
print('\n')

# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')
# 6B. Comment your code in 6A to convince yourself you understand how it works
# The np. random function allows you to specify a single element in a list.
import numpy as np
print(f'A random number between 0 and 1:')
print(np.random.rand(1))

'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 
Remember to comment all your code and push your work to your Github repo when you're done!
'''
