print("Challenge 3.2: Playing with the stock market")
# Creating individual variables which store the approximate market price of 5 companies; Amazon, Apple, Facebook, Google and Microsoft.
amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200


print("Challenge 3.2.1: Taking user input")
# Creating code/variable to prompt the client/user the ability to enter her name and save it to a variable.
# Creating code/variable to prompt the client/user the ability to enter her savings and save it to another variable.
# Creating code/variable to prompt the client/user the ability to enter the stock she is interested in and save it to a variable.
name = input("What is your name?")

# extra points for checking errors in the user input
savings = int(input("How much savings do you have?"))
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")


print("Challenge 3.2.2: Perform user-specific calculations")
#Creating conditional code in the form of (if-elif-else) statements to compute the number of stocks of the company that can be purchased with the savings amount.
number_of_stocks = 0
if stock == "amzn": 
    price = amazon 
    number_of_stocks = savings/price 

elif stock == "aapl": 
    price = apple 
    number_of_stocks = savings/price 

elif stock == "fb": 
    price = fb 
    number_of_stocks = savings/price 

elif stock == "goog": 
    price = google 
    number_of_stocks = savings/price 

elif stock == "msft": 
    price = msft 
    number_of_stocks = savings/price 

else: 
    price = "NA" 


print("Challenge 3.2.3: Output for the user the result")
# Creating code to print the result for the client/user in this format: "Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100".
if price == "NA": 
    print("Incorrect stock name entered.") 

else: 
    print(f"{name} has ${savings} in savings and she can buy {number_of_stocks} shares of {stock} at the current price of ${price}.")
