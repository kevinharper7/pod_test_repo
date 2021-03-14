# Create a code for the food, tip amount and number of people splitting the bill

dinner = float(input("How much did your dinner cost:\n "))
tip = int(input("Enter you tip %:\n "))
tax = .08 
party_size = int(input('Number of friends in party:\n '))
print(party_size)

# Calculations
tax_amount = dinner * tax
tip_amount = dinner * tip/100
total = dinner + tip_amount + tax_amount
total_per_person = total/party_size

print(f"\nThe dinner was ${dinner:.2f}.\n")
print(f"\nEach one of you bozo's should pay ${total_per_person:.2f}.\n")
print(f"The tip was ${tip_amount:.2f}.\n")
print(f"The total cost of your dinner was ${total:.2f}.\n")




 