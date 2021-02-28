name = input('What is your name?')
print(f'Hello {name}!') 

allergy = input('Are you allergic to cats or dogs?')
if allergy == "yes":
    print('Aw thats too bad!')
else:
    print('Fantastic!')

like_dogs = input('Do you like dogs?')
if like_dogs == "yes":
    print('Woof woof! Dogs rock!')
else:
    print('Thats totally understandable!') 

dog_small_big = input('If you could have a dog, would it be small, medium or big?')
if dog_small_big == "small":
    print('Thats adorable!')
elif dog_small_big == "big":
    print('I love big dogs!')
else:
    print('All dogs are great!')

have_dog = input('So, do you have a dog?')
if have_dog == "yes":
    print('Aw i would love to meet them!')
else:
    print('Having a dog would make a great companion!')

how_many_dogs = input('If you could, how many dogs would you like to have?')
how_many_dogs_int = int(how_many_dogs)
if how_many_dogs_int == 1:
    print('1 would be awesome!')
elif how_many_dogs_int > 1:
    print('The more the merrier!')
else:
    print('Thats ok! Nothing wrong with that!')

prefer_cat = input('Would you prefer a cat?')
if prefer_cat == "yes":
    tabby = input('Like a tabby?')
    if tabby == "yes":
        print('Tabbies are awesome!')
    else:
        print('Ok, I totally understand!')
else:
    print('I like dogs better too!') 

have_cat = input('Do you have a cat?')
if have_cat == "yes":
    print('Cats are great!')
else:
    print('Maybe you can consider adopting one in the future!')

how_many_cats = input('If you could, how many cats would you like to have?')
how_many_cats_int = int(how_many_cats)
if how_many_cats_int == 1:
    print('Aw thats cute!')
elif how_many_cats_int > 1:
    print('Wow! That would be so much fun!')
else:
    print("No problem! Cats aren't for everyone!")

print('Thank you for taking this survey!')