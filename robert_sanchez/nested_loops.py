# Nested Logic
# Logical statement inside logical statement
# Nested if statements

a = 1

if a > 1:
    print('above 1')

    # inner level of logic
    # will only get run if a> 1

    if a > 2:
        print('above2')
    else:
        print('below 2')

else:
    print('below 1')

    # Nest logice inside a loop

    #If statement inside a loop

num_list = [9,3,5,-2, 4, -5, -1, 8]

# loop through num list, and print out positive numbers only

for number in num_list:
    if number > 0:
        print(number)
else:
    print('NEGATIVE')
num_list = [9,3,5,-2, 4, -5, -1, 8]

# break stops the loop immeadiately
# print out numbers until I hit a negatice, then stop

for number in num_list:
    if number > 0:
        print(number)
    else:
        break

    print('fully nested loop')

day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

for day in days:
    for meal in meals:
        print(f'{day}', {meal})

for meal in meals:
    for day in days:
        print(f'{meal}, {day}')

password = 'bronx'
logged_in = False

while logged_in = False:
   if user_resp ==password:
    print('logged in')
    logged_in = True 

# this code will only run if the password is wrong

print('Incorrect password')