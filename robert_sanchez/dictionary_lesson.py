# evert dictionary is enclosed in curly braces

empty_dict = {}
print(type (empty_dict))

#set up bank accout dictionary
#sytax for dictionary items is key:value
user_account = { 'username' : 'pito', 'balance' : 300.76}

print(user_account)

# Retrieving specific values from the dictionary
# We get *specfic* values from the dictionary using dictionary_variable_name[<key>]
# This is like LOOKING SOMETHING UP in a physical dictionary

print(user_account['username'])

my_username = user_account ['username']
print(my_username)


#add a new item to a dictionary (adding a new key:value pair)
#dictionary_variable_name[<key that doesn't exist yet>] = <new data to assign>

user_account['last_transaction_date'] = '9/15/2020'

user_account['account_verified'] = True
print(user_account)

# Udating dictionary items
# dictionary_variable_name[<key that DOES EXIST>] = <NEW DATA TO ASSIGN>
user_account['last_transaction_date'] = '2/9/2021'
print(user_account['last_transaction_date']

# Remove items from a dictionary
# dictionary_variable_name.pop(<key that Does exist>)

user_account.pop('last_transaction_date')

#adding to a dictionary using user input
user_account['account_password'] = ('create a new password here: ')
