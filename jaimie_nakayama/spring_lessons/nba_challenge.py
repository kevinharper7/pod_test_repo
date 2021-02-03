print("Challenge 2.1:")
jamal_murray_3pts_made = 46
fred_vanvleet_3pts_made = 43
james_harden_3pts_made = 37

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots.")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} 3 point shots.")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots.")

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
jamal_murray_3pts_attempted = 93
fred_vanvleet_3pts_attempted = 110
james_harden_3pts_attempted = 109

print("Challenge 2.4: Build on your print statement")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots and {jamal_murray_3pts_attempted} 3 point shot attempts.")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} 3 point shots and {fred_vanvleet_3pts_attempted} 3 point shot attempts.")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots and {james_harden_3pts_attempted} 3 point shot attempts")

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
jamal_murray_3pt_percentage = 49.46
fred_vanvleet_3pt_percentage = 39.09
james_harden_3pt_percentage = 33.94
print(f"Jamal Murray made {jamal_murray_3pt_percentage}% of his 3 point shots.")
print(f"Fred VanVleet made {fred_vanvleet_3pt_percentage}% of his 3 point shots.")
print(f"James Harden made {james_harden_3pt_percentage}% of his 3 point shots.")

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
print("The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \nThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. \nThey were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.")

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
message = "The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \nThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. \nThey were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season."
print(message.upper())

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
lakers_are_best = True
print(f"The Lakers are the best basketball team in the NBA. {lakers_are_best}.")

print('Challenge 3.4: Type Conversion')
print(int(lakers_are_best))
# true statements return 1
print(float(lakers_are_best))

print('Challenge 3.5: Type Conversion Part 2')
print(str(jamal_murray_3pt_percentage))
print(str(fred_vanvleet_3pt_percentage))
print(str(james_harden_3pt_percentage))
# nothing changed in the variable when converted into a string
print(int(jamal_murray_3pt_percentage))
print(int(fred_vanvleet_3pt_percentage))
print(int(james_harden_3pt_percentage))
# the variable was rounded down when converted into an integer