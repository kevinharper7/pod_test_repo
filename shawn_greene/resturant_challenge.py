print("Challenge: Favourite Restaurants")
print()

print("Question 1")

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp. 
Go through the dictionary and print out the following 3 pieces of information about the restaurant: 
1. The latitude and longitude of Four Barrel Coffee 
2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code. 
3. The website of Four Barrel Coffee
'''


restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}

print(f"{restaurant['latitude']}, {restaurant['longitude']}")

#(restaurant['address'], restaurant['city'], restaurant['state'], restaurant['zip code'])
print(f"{restaurant['address1']}, {restaurant['city']}, {restaurant['state']}, {restaurant['zip_code']}")

print(restaurant['url'])
# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
# TODO: Write code to print the URL of the website of Four Barrel Coffee.






print("Question 2")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)

# TODO: Print each dictionary

# The dictionary for each restaurant should look something like this

'''
restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich" }
'''
#Randy's 123 1st st, NY 10016, pizza
#Kate's 456 2nd st, NY 10016, lobster
#Mickey's 789 3rd st, NY 10016, hamburger

location = "It is located at"
fav = "My favorite dish there is"

RN = "Randys"
RA = "123 First st, NY 10016"
RFD = "pizza"

KN = "Kate"
KA = "456 Second st, NY 10016"
KFD = "lobster"

MN = "Mickey"
MA = "789 Third st, NY 10016"
MFD = "hamburger"
 

R_info = f"My favorite restaurant within NYC is {RN}. {location} {RA}. {fav} {RFD}"
print(R_info)
K_info = f"My second favorite restaurant within NYC is {KN}. {location} {KA}. {fav} {KFD}"
print(K_info)
M_info = f"My third favorite restaurant within NYC is {MN}. {location} {MA}. {fav} {MFD}"
print(M_info)


Randy_file = {'name':'Randy', 
              'address' :'123 First st, NY 10016','fave' : 'pizza'}                        
#print(Randy_file)
Kate_file = {'name':'Kate', 
              'address' :'456 Second st, NY 10016','fave' : 'lobter'}  
#print(Kate_file)
Mickey_file = {'name':'Mickey', 
              'address' :'789 Third st, NY 10016','fave' : 'hamburger'}  
#print(Mickey_file)


print("Question 3")
print(Randy_file)
print(Kate_file)
Mickey_file.pop('fave')
print(Mickey_file)




#Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there. 
#Remove the 'favourite_dish' key value pair from that restaurant's dictionary



# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant


print("Question 4")
print(Randy_file)
Kate_file['address'] = '123 Main st NY, 10016'
print(Kate_file)
print(Mickey_file)

#Kate_file['address'] = '123 Main st NY, 10016'
#print(Kate_file['address'])

#print(user_account['balance'])
#user_account['last_trasaction_date'] = '2/9/2021'
#print(user_account['last_transaction_date'])

#Imagine that another one of your most favourite restaurants modified its address. 
#Update just this value in that restaurant's dictionary


# TODO: Update the address field of 1 restaurant 
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
# TODO: Print the updated dictionary.

