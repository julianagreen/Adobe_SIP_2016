import random
from turtle import *

penup()
goto(-200, -150)

option1 = "chargers"
option2 = "jellybeans"
option3 = "rainbow"
option4 = "adobe"

x_tally = -150

word_options = [option1, option2, option3, option4]

index_option = random.randint(0, len(word_options)-1)

for i in range(len(word_options[index_option])):
    pendown()
    forward(50)
    penup()
    forward(15)

right(90)


for i in range(len(word_options[index_option]) + 6):
    letter = input("What letter would you like to guess? ")
    if letter in word_options[index_option]:
        print("You guessed right!")
        print(letter)
    else:
        print("You guessed wrong, try again")
        penup()
        goto(x_tally, 200)
        pendown()
        forward(40)
        x_tally += 20
    
