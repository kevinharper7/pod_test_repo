lyrics = "Hey Ya!"
#print(lyrics)

ny_num=3
str_num = '3'
#as long as it has quotes it can be a string
#print(str_num)


long_lyrics = "At first I was afraid, I was petrified, \nKept thinking I could never live without you by my side, \nBut then I spent so many nights thinking how you did me wrong, \nAnd I grew strong"
#print(long_lyrics)


long_lyrics_2 = "At first I was afraid, I was petrified, \tKept thinking I could never live without you by my side, \tBut then I spent so many nights thinking how you did me wrong, \tAnd I grew strong"
#long_lyrics_2 = "At first I was afraid, I was petrified,[\t]Kept thinking I could never live without you by my side, [\t]But then I spent so many nights thinking houw you did me wrong, [\t]And I grew strong"

#print(long_lyrics_2)



sale = 18.00
message = "This is great news"
#concantanate example

ex_1 =  "Today's sale is" + "18.00"
#print(ex_1)

#example 2 f (string)

ex_2 = f"Today's sale is {sale}. {message}"
print(ex_2)

#strings have functions

hello = "hello world, this is shawn"
hello_2 = "Hello world, this is not shawn"
#print(hello.upper())
#print(hello_2.lower())

hello_upper = hello.upper()
print(hello)
print(hello_upper)