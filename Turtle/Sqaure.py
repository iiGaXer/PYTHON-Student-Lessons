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

side_length = 5

# for i in range(4):  # for (int i = 0; i < 4; i++) ()
    # print(i)
   # t.fd(side_length)   # Forward: pixels
   # t.rt(90)            # Right Turn: degree

def draw_sqaures():
    global side_length
    for i in range(8):   # for (int i = 0; i < 4; i++) ()
        t.fd(side_length)   # Forward: pixels
        t.rt(45)

# Makes/draw 10 sqaures
for i in range(200):
    t.penup()
    t.goto(randint(-683,384), randint(-683,384))
    t.pendown()
    side_length = randint(10, 100)
    draw_sqaures()
    



turtle.done()