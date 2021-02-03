print("Challenge 2.1")
# create variables
jamal_murray_3pts_made = 46
fred_vanvleet_3pts_made = 43
james_harden_3pts_made = 37

print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots.")
print(f"In the 2020 NBA playoffs, Fred Vanvleet made {fred_vanvleet_3pts_made} 3 points shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")

print("Challenge 2.3")
#create variables for 3 point shot attempts
jamal_murray_3pts_att = 93
fred_vanvleet_3pts_att = 110
james_harden_3pts_att = 109

print(f"In the 2020 playoffs, Jamal Murray had {jamal_murray_3pts_att} 3 point attempts")
print(f"In the 2020 playoffs, Fred Vanvleet had {fred_vanvleet_3pts_att} 3 point attempts")
print(f"In the 2020 playoffs, James Harden had {james_harden_3pts_att} 3 point attempts")


print("Challenge 2.5 Calculate, store, and print the three point percentage for each player")
# calculate 3 point percentage
jamal_murray_3pt_per = jamal_murray_3pts_made / jamal_murray_3pts_att
fred_vanvleet_3pt_per = fred_vanvleet_3pts_made / fred_vanvleet_3pts_att
james_harden_3pt_per = james_harden_3pts_made / james_harden_3pts_att
print("Jamal_Murray")
print(jamal_murray_3pt_per)
print("Fred_Vanvleet")
print(fred_vanvleet_3pt_per)
print("James_Harden")
print(james_harden_3pt_per)


print("Challenge 3.1")
# add escape characters to long sentence
print("The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, \nand 3 first-round picks to New Orleans to land Davis. \nThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, \nand company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, \nto the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. \nThey were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers \nto rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball \nand are in a position to have another successful year next season.")

# capitalize all letters, one sentence per line
print("Challenge 3.2")
long_sentence = "The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, \nand 3 first-round picks to New Orleans to land Davis. \nThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, \nand company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, \nto the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. \nThey were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers \nto rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball \nand are in a position to have another successful year next season."
print(long_sentence.upper())


print("Challenge 3.3")
# create boolean variable
lakers_are_best = True
print(f'the lakers are the best basketball team in the NBA {lakers_are_best}')

print("Challenge 3.4 Type Conversion")
# convert variable into integer
print(int(lakers_are_best))
# best coresponds to number 1 ranking
print(float(lakers_are_best))
# adds zero decimal place

print('Challenge 3.5 Type Conversion type 2')
# Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
print(f" In the 2020 NBA playoffs Jamal Murray shot {jamal_murray_3pt_per} percent from 3")
print(f" In the 2020 NBA playoffs Fred Vanvleet shot {fred_vanvleet_3pt_per} percent from 3")
print(f" in the 2020 NBA playoffs James Harden shot {james_harden_3pt_per} percent from 3 ")
# answers still have carrying decimal
# convert to integer

print(int(jamal_murray_3pt_per))
print(int(fred_vanvleet_3pt_per))
print(int(james_harden_3pt_per))
# rounds down to nearest whole number which is 0
