'''
Planning & pseudocode challenge!
For each piece here, write out the pseudocode as comments FIRST, then write your code!
At many points, you'll have to choose between using a list vs. dictionary. Justify your choices!
'''


'''
1. Shipping
You are building a system to handle shipping orders. Each order should have 3 pieces of information:
-destination (string) (for the purposes of this challenge this can be any place, no need to make a full address)
-date_shipped (string)
-weight (float) (how many pounds the package is)
Will you choose to make each shipping order as a dictionary or list? Why?
Assign 3 separate orders to 3 separate variables
'''
print('\nPART 1')

''' 
Each order will have 3 pieces of information, so I would make it a dictionary.
Setting each order (dictionary) with 3 key:value pairs
First the destination (string)
Second the date shipped (string)
Last the weight (float)

Do this 3 times for 3 seperate orders (total of 3 dictionaries).
Assign each dictionary to their own variable.
'''
order_1 = {'Destination': 'Mexico', 'Date shipped': '3/2/21', 'Weight': 1.27}
order_2 = {'Destination': 'St. Lucia', 'Date shipped': '3/4/21', 'Weight': 5.62}
order_3 = {'Destination': 'Aruba', 'Date shipped': '2/28/21', 'Weight': 1.03}

'''
2. Building the database
Now, let's put the orders all into a database togther (all the orders are stored in 1 variable). 
Your database as a whole can either be a dictionary or a list (hint, you'll want nesting!). 
Print out the database to make sure all the info is in there. 
'''
print('\nPART 2')

'''
Placing all 3 orders into a single database with 1 variable. I'd make a list, since I dont need key:value pairs.
Create variable order_database with list of order_1, order_2, and order_3 variables.
'''

order_database = [order_1, order_2, order_3]

print(order_database)
'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')

'''
Create a new variable order_4 with a dictionary that has the 3 key value pairs: destination, date shipped and weight.

Create new function called add_order() with 2 parameters (order_database, order)
Append the new order to order_database
Call add_order () the print order_database
'''
order_4 = {'Destination': 'Maldives', 'Date shipped': '3/10/21', 'Weight': 2.00}

def add_order(order_database, order):
    order_database.append(order)

add_order(order_database, order_4)
print(order_database)

'''
4. Define a function called complete_order() to mark a specific order in your database complete
This means you'll need a new piece of data inside the order that is True when the order is complete.
Test this out and print out your database to make sure it works!
HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
print('\nPART 4')

'''
Define a function called complete_order with 2 variables order_database and order_index
Add 'Complete' key and set value to True
Call complete_order function then print order_database
'''

def complete_order(order_database, order_index):
    order_database[order_index]['Completed'] = True

complete_order(order_database, 0)
print(order_database)