import turtle
from random import randint
# Set the background color
screen = turtle.Screen()
screen.bgcolor('black')   # black
# Create a turtle
# t = turtle.Turtle(visible=False)
t = turtle.Turtle()
# t.width(1)
# t.color('red')
t.color("blue") 
t.speed(50)
# t.hideturtle()

side_length = 1

for i in range(65):
    t.circle(50)
    t.rt(10)
    t.rt(side_length)
    



turtle.done()