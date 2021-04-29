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
Each order will contain a:
destination which will be a string, a
date_shipped which will also be a string, and a
weight which will be a float.

'''
# I am choosing to create a dictionary instead of a listbbecause dictionaries allow me to use lables. 
# I am also assigning 3 separate orders to the 3 separate variables created.
order_1 = {'destination' : 'New York','date_shipped' : '03/11/2021','weight' : 5}
order_2 = {'destination' : 'California','date_shipped' : '03/11/2021','weight' : 5}
order_3 = {'destination' : 'Texas','date_shipped' : '03/11/2021','weight' : 5}
print(order_1)
print(order_2)
print(order_3)

'''
2. Building the database
Now, let's put the orders all into a database togther (all the orders are stored in 1 variable). 
Your database as a whole can either be a dictionary or a list (hint, you'll want nesting!). 
Print out the database to make sure all the info is in there. 
'''

print('\nPART 2')
'''I will create a single variable and database to put all of the orders into.
'''

# Here I am creating a database by using 'order_database' as a variable, 
# in a list that includes each of the orders to complete the database.
order_database = [order_1, order_2, order_3]
print(order_database)

'''

'''
'''3. Define a function called add_order() that adds one more order to your database, 
and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')

# Defining an "add_order" function to facilitate the process of adding more orders,
# to be included in the database as needed using the append function, which will work 
# because this a list and not a dictionary.
def add_order(order_database, order):
    order_database.append(order)

# Creating two new orders that include all order information same as previous orders.
order_4 = {'destination' : 'Guam','date_shipped' : '03/12/2021','weight' : 10.5}
order_5 = {'destination' : 'Prague','date_shipped' : '03/12/2021','weight' : 10.5}

# Adding the two new orders to the order_database in the same format as the previous orders.
order_database.append(order_4)
order_database.append(order_5)
print(order_database)

'''

4. Define a function called complete_order() to mark a specific order in your database complete
This means you'll need a new piece of data inside the order that is True when the order is complete.
Test this out and print out your database to make sure it works!
HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database

'''
print('\nPART 4')
# Creating a variable called 'complete_order' and defining the complete_order function to designate 
# specific orders as completed using booleans True/False.
# I have to create a variable that defines each order's status, 
# in the form of a boolean questioning whether order is complete : True or False, if True...
def complete_order(order_database, order):
    order_database[order]['complete'] = 'True'

# I am going to print at this point to make sure the coding works before I continue.
print(complete_order)

# I can create a variable that lists all of the complete orders, 
# such as 'complete_order_list' and print out a list of all of the completed orders, 
# then reference specific orders in that list by item number based on where they exist 
# in the new list: ie., [0,1,2,3, etc.].


def complete_order_list(order_database, order):
    order_database[order]


# Running to make sure coding works for the variable 'complted_orders_list'.
print(complete_order_list)


