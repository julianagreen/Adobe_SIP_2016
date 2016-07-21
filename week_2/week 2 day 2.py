from turtle import *


xPos = -150
yPos = 100

def draw_shape(color, num_sides, side_length):
    penup()
    goto(xPos, yPos)
    pendown()
    pencolor(color)
    for i in range(8):
        for i in range(num_sides):
            forward(side_length)
            right(360/num_sides)
        penup()
        forward(80)
        right(5)
        pendown()
    xPos += 20
    yPos -= 10

list1 = ["red", "blue", "green", "orange", "purple"]

for item in list1:
    draw_shape(item, 3, 200)
