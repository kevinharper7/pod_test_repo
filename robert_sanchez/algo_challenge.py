# Algorithmic Challenge


print("Question 1")
print()

fruit_list = ["apple", "orange", "banana", "pear", "grape", "pineapple"]
fruit = "pear"
 # Write the time complexity for the function below, check_if_fruit_in_list

def check_if_fruit_in_list(my_list, fruit):
    for fruit_item in my_list:
        if fruit_item == fruit:
            print("Fruit in list!")
    print("Fruit not in list!")


 # TODO Write the time complexity
 # Time complexity is O(n) # this linear


 # For Questions 2 and 3, we are going to look at the time complexities for the previous deli meats challenge

meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

print("Question 2")
print()
 # Write the time complexity for the function below, capitalize_meats_and_cheeses
def capitalize_meats_and_cheeses(meats, cheeses):
    for i in range(len(meats)):
        meats[i] = meats[i].capitalize()

    for i in range(len(cheeses)):
        cheeses[i] = cheeses[i].capitalize()
    print(meats,cheeses)

 # TODO Write the time complexity
 # Time complexity is O(n)


print("Question 3")
print()
 # Write the time complexity for the function below, deli_meat_challenge # Nested data
def deli_meat_challenge(meat, cheeses, sandwiches):
    for meat in meats:
        for cheese in cheeses:
            sandwiches.append(f'{meat} & {cheese}')
    return sandwiches

 # TODO Write the time complexity
 # Time complexity is O(n^2) #Quadratic



print("Question 4")
print()

'''
 For the following question, you will be given an unsorted array that may contain duplicates. 
 Your job is to write a function that returns true if there are duplicates and false if not.
 Then write the time complexity of that function and think of if there are anyways you could have
 made the algorithm more efficient? 

 return True if there is a duplicates, False if there are no duplicates in the list
''' 
my_list = [2,6,3,4,5,8]
def contains_duplicates(my_list):
    if len(my_list) != len(set(my_list)):
        print(True)
    print(False)
contains_duplicates(my_list)


 # Bonus
def contains_duplicates_linear(my_list):
    seen = {}
    for item in my_list:
        if item in seen:
            return True
            seen[item] = item
    return False

 # Time Complexity is O(n) # Linear
