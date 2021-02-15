# looping through a list of intergers

numbers = [12, 8, 44, -5]

for number in numbers:
    print(number)

    # Things to remember about loops:

    # variable comes right after 'for' is the *interator variable*
    # variable that comes
    # things INSIDE the loop are indented

    for number in numbers:
        [number]
        print('hi computer') 

    # Loop through strings
    grocery_list = ['eggs', 'apples', 'cheese', 'juice']
    for food in grocery_list:
        print(food)

list_sum = 0
numbers = [12, 8, 44, -5]
for number in numbers:
    new_number = number*2
    print(new_number)

#adding all the numbers in the list



for number in numbers: 
    list_sum = list_sum + number
    print(list_sum)

# make a capitalized grocery list
grocery_list = ['eggs', 'apples', 'cheese', 'juice']

grocery_caps = []

for food in grocery_list:
    grocery_caps.append(food.upper())
print(grocery_caps)

# use loops with the rand() function



# range(n) - makes a sequence of intergers from 0 up to not
        not including n 

for num in range(10):
    print(num)
