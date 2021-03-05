# DO NOT WORRY ABOUT THE LINES BELOW THIS LINE
def format_currency(amount: float) -> str:
    return "${:,.2f}".format(amount)
# DO NOT WORRY ABOUT THE LINES ABOVE THIS LINE
format = format_currency

print("\n")
# Applying a clear title statement to indicate the use of this code to potential users; "The Super Easy-Super Accurate Tip_Calculator")
print("The Super Easy & Super Accurate Tip Calculator")
# This ("\n") is used threoughout this code to create a line separation, and give the code some clarity for the end user/reader.
print("\n")

# Code created to allow the user to input the restaurant check subtotal, which will convert the amount from a string to a float.
check_subtotal_str = input("> Enter the restaurant check subtotal amount (for example: 50.00, 100.75 25.50, etc.): ")
check_subtotal_float = float(check_subtotal_str)

# Code created to allow the user to input the restaurant check sales tax, which will convert the amount from a string to a float.
check_tax_str = input("> Enter the restaurant check sales tax amount (for example: 5, 10 25.50, etc.): ")
check_tax_float = float(check_tax_str)

# Code created to allow the user to input the restaurant check grandtotal amount, which will convert the amount from a string to a float.
check_grandtotal_str = input("> Enter the restaurant check grandtotal amount to be split (for example: 5, 10 25.50, etc.): ")
check_grandtotal_float = float(check_grandtotal_str)

# Code created to allow the user to input and designate the number of people splitting the restaurant check and convert that number from a string to an integer.
number_people_str = input("> Please enter the number of people splitting this restaurant check: ")
number_people_int = number_people_str

# Code created to allow the user to input a percentage of the restaurant check grandtotal to tip, and convert this percentage from a string to a float.
tip_percent_str = input("> Enter the desired tip amount percentage (for example: 10, 15, 20.50, etc.): ")
tip_percent_float = float(tip_percent_str)
print("\n")

# Code created to allow the user to confirm the input information as correct or incorrect.
print(f"You are splitting the restaurant check grandtotal in the amount of {format_currency(check_grandtotal_float)} among {number_people_int} people with a {tip_percent_float}% tip.")
print("\n")

# Code created to allow the user to confirm the input information as correct or incorrect by indicating "yes" or anything other than "yes".
confirm_input = input("> Type yes if all of the information that have been input is correct, or any other key if it is incorrect ")
correct_input = confirm_input == 'yes'
print("\n")


# Code created to split restaurant check grandtotal amount by, the number of people splitting the check, and print the result amount.
amount_per_person = float(check_grandtotal_float)/float(number_people_int)
# print(f"Restaurant check grandtotal divided by # of people splitting check = {format_currency(amount_per_person)}")
print(amount_per_person)

# Code created to calculate the tip amount per person by multipliny the check grandtotal amount per person by the tip percentage.
tip_per_person = float(amount_per_person) * float(tip_percent_float/100)
# print(format_currency(tip_per_person))
print(f"Tip per person = {format_currency(tip_per_person)}")
print(tip_per_person)


# Code created to calculate the grandtotal check amount per person by adding the restaurant check subtotal amount, tax amount per person with the tip percentage amount per person.
total_per_person = float(amount_per_person) + float(tip_per_person)
# print(f"Total per person = {format_currency(total_per_person)})


print(f"Each person splitting the restaurant check should pay {format_currency(total_per_person)}!'How's that for accuracy?!!'")
print("\n")