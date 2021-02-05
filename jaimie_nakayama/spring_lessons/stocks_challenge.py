print("Challenge 3.2: Playing with the stock market")

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200



print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
# TODO: Write code to ask the client his savings and save it to another variable.
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
name = input("What is your name?")
savings = int(input("How much do you have in savings?"))
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''

if stock == "amzn":
    num_of_stocks = (savings // amazon) 

elif stock == "aapl":
    num_of_stocks_apple = (savings // apple)

elif stock == "fb":
    num_of_stocks_fb = (savings // fb)

elif stock == "goog":
    num_of_stocks_goog = (savings // google)

elif stock == "msft":
    num_of_stocks_msft = (savings // msft)

else:
    print("Not applicable!")

print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

if stock == "amzn":
 print(f"{name} has {savings} in savings and he can buy {num_of_stocks} share of Amazon at the current price of $3000.")

elif stock == "aapl":
 print(f"{name} has {savings} in savings and he can buy {num_of_stocks_apple} shares of Apple at the current price of $100.")

elif stock == "fb":
 print(f"{name} has {savings} in savings and he can buy {num_of_stocks_fb} shares of Facebook at the current price of $250.")

elif stock == "goog":
 print(f"{name} has {savings} in savings and he can buy {num_of_stocks_goog} shares of Google at the current price of $1400.")
else:
 print(f"{name} has {savings} in savings and he can buy {num_of_stocks_msft} shares of Microsoft at the current price of $200.")
