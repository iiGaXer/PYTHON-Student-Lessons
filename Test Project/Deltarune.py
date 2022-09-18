import turtle
import time
import getpass
import sys
from random import randint

# Set the background color
screen = turtle.Screen()

# Title the game
screen.title("Deltarune")

# giving a variable a value: turtle variable, important
t = turtle.Turtle()

# Makes the background image this image
screen.bgpic("background.png")

# Register's an image
screen.register_shape("Kris.gif")

# declares and puts this image
t.shape("Kris.gif")

# The name of the player

# Choice: if they typed no
def No():
    screen.textinput("Then.....", "*???")
    screen.update()
    time.sleep(1.5)
    screen.bgpic("background3.gif")
    screen.register_shape("chara.gif")
    t.shape("chara.gif")
    screen.textinput("why are you here =)", "✡□◆︎ ■♏♏♎︎ ⧫□︎ ⬧⧫♋⍓︎ 👎︎︎☜☜❄︎☜︎☼💣︎✋︎✋︎☠☜︎👎︎"    )
    screen.title("GAME OVER =)")
    turtle.clear()
    sys. exit()

# Choice: If they typed yes    
def Yes():
    screen.textinput("Excellent", "...")
    time.sleep(1.5)
    screen.textinput("Truly excellent", "...")
    time.sleep(1.5)
    if screen.textinput("What is your name?", "Vessel:") == "Gaster":
        screen.title("VOID")
        screen.update()
        time.sleep(1.5)
        screen.bgpic("void.gif")
        screen.register_shape("gaster.gif")
        t.shape("gaster.gif")
        screen.textinput("GASTER", "✋︎■︎⧫︎♏︎❒︎♏︎⬧︎⧫︎♓︎■︎♑︎📬︎📬︎📬︎")
        sys. exit()
    time.sleep(2)
    screen.textinput("Excellent... ", "*You took the compliment")
    time.sleep(2)
    if screen.textinput("What is your soul trait?", "*DETERMINATION, BRAVERY, INTERGRITY, JUSTICE, PERSERVERIENCE or KINDESS?") == "DETERMINATION":
        time.sleep(2)
        screen.textinput("Oh..?", "*You are filled with DETERMINATION")
        screen.textinput("Then...", "*...")
        time.sleep(2)
        screen.bgpic("background3.gif")
        screen.register_shape("chara.gif")
        t.shape("chara.gif")
        screen.title("GAME OVER =)")
        screen.textinput("Your soul....is mine to control =)", "*GAME OVER")
        sys. exit()
    time.sleep(2)
    screen.textinput("Good....", "...")
    time.sleep(2)
    screen.textinput("*You are ready", "Now lets take your creation...")
    screen.update()
    time.sleep(2)
    t.hideturtle()
    screen.bgpic("creepy kris.gif")
    screen.textinput("And throw it away...", "*You feel like your being controlled")
    time.sleep(2)
    screen.textinput("No one gets to chose who they are", "*You are feeling like this isn't the first time")
    
# If they cannot chose
def Dumb_responce():
    screen.textinput("*You chose to say something...", "You know....your REALLY getting on my bad side")
    time.sleep(2)
    screen.update()
    screen.bgpic("background3.gif")
    screen.register_shape("chara.gif")
    t.shape("chara.gif")
    screen.textinput("Die. =)", "✡□◆︎ ■♏♏♎︎ ⧫□︎ ⬧⧫♋⍓︎ 👎︎︎☜☜❄︎☜︎☼💣︎✋︎✋︎☠☜︎👎︎")
    screen.title("GAME OVER =)")
    sys. exit()

# The file location of any pics needed in a future project :):

# C:\Users\mahfu\AppData\Local\Programs\Python\Python38-32

# Delays code for what's in ()
time.sleep(2)
# Text box: type an anwser
screen.textinput("Hello.....", "*You are nervous..")
# Delays code for what's in ()
time.sleep(2)
# Text box: type an anwser
screen.textinput("Are we.....connected?", "*You don't know what to say")
# Delays code for what's in ()
time.sleep(2)

# If the choice is yes: this statement executes the "No()" function
if screen.textinput("*Choose:", "*No....or Yes?") == "No":
    No()
# Else if the choice is Yes this statement executes the "Yes()" function
if screen.textinput("Final desicion:", "*No....or Yes?") == "Yes":
        Yes()
# Else

else:
    Dumb_responce()

# The beginging of the game
screen.update()
screen.setup(550, 427)
time.sleep(1.3)

def fxn():
    turtle.penup()
    turtle.forward(20)
    sc.register_shape("walking.gif")
    turtle.shape("walking.gif")
    turtle.forward(10)
    time.sleep(0.1)
    sc.register_shape("walkingn.gif")
    turtle.shape("walkingn.gif")
    turtle.forward(10)
    time.sleep(0.1)
    sc.register_shape("walking.gif")
    turtle.shape("walking.gif")
      
def fxn1():
    turtle.penup()
    turtle.right(90) 
  
def fxn2():
    turtle.penup()
    turtle.left(90)
    sc.register_shape("up.gif")
    turtle.shape("up.gif")
    turtle.left(10)
    time.sleep(0.1)
    sc.register_shape("up2.gif")
    turtle.shape("up2.gif")
    turtle.left(10)
    time.sleep(0.1)
    sc.register_shape("up.gif")
    turtle.shape("up.gif")
    
# set screen size 
sc = turtle.Screen() 
sc.setup(500,300) 
  
# call methods
turtle.onkey(fxn,'space')
turtle.onkey(fxn1,'Right') 
turtle.onkey(fxn2,'Left') 
 
# to listen by the turtle 
sc.textinput("Instructions:", "space to move forward, right to move to right, and left to move to left")

t.showturtle()
screen.bgpic("bedroom.gif")
screen.register_shape("walking.gif")
t.shape("walking.gif")
turtle.listen()
