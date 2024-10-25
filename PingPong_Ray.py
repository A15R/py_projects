from turtle import *
from time import sleep
import random
import math
from tkinter import messagebox


ini_x_cor=random.choice([-600,+600])
ini_y_ran=random.randint(-299,+299)
score_card_a=0
score_card_b=0

tur3=Turtle()#Turtle object for scorecard A.
tur3.color("white")
tur3.hideturtle()
tur3.penup()
tur3.goto(+40,209)

tur4=Turtle()#Turtle object for scorecard B.
tur4.color("white")
tur4.penup()
tur4.hideturtle()
tur4.goto(-80,209)

screen = Screen()#Screen object.
screen.bgcolor("black")
screen.screensize(1200,600)
screen.title("PONG")

ball=Turtle(shape='circle')#Ball object.
ball.left(90)
ball.color("orange")
ball.shapesize(1,1)
ball.penup()

bar1= Turtle(shape="square")#Paddle or bar object A.
bar1.teleport(+600,0)
bar1.shapesize(5,1)
bar1.color("white")

bar2= Turtle(shape="square")#Paddle or bar object B.
bar2.teleport(-600,0)
bar2.shapesize(5,1)
bar2.color("white")

def upA():
    """Down movement of bar1/barA"""
    bar1.penup()
    if bar1.ycor() > +209:
        return
    else:
        bar1.goto(bar1.xcor(),bar1.ycor()+20)

def downA():
    """Down movement of bar1/barA"""
    bar1.penup()
    if bar1.ycor() < -209:
        return
    else:
       bar1.goto(bar1.xcor(),bar1.ycor()-20)
    
screen.onkeypress(fun=upA,key="Up")#Keys press movement of bar commands for A.
screen.onkeypress(fun=downA,key="Down")

def upB():
    """Upwards movement of bar2/barB"""
    bar2.penup()
    if bar2.ycor() > +209:
        return
    else:
        bar2.goto(bar2.xcor(),bar2.ycor()+20)
    
def downB():
    """Downwards movement of bar2/barB"""
    bar2.penup()
    if bar2.ycor() < -209:
        return
    else:
       bar2.goto(bar2.xcor(),bar2.ycor()-20)

screen.onkeypress(fun=upB,key="w")#Keys press movement of bar commands for B.
screen.onkeypress(fun=downB,key="s")
screen.listen()

collision_a=False
collision_b=False
def motion():
    """Gives the ball the bounce off the top\n
    and bottom edges functionality"""
    leen=math.copysign(1,ball.xcor())
    global collision_a
    global collision_b
    if leen == 1:
            collision_a=True
            ball.speed(2)
            ball.goto(random.randint(+100,+499),+299)
            ball.goto(random.randint(-499,-100),-299)
            ball.speed(2)
    elif leen == -1:
            collision_b=True
            ball.speed(2)
            ball.goto(random.randint(-499,-100),+299)
            ball.goto(random.randint(100,+499),-299)
            ball.speed(2)
    else:
        raise "some error in motion function code"
    
def dotted():
    """Separation in between the sides"""
    dot=Turtle()
    dot.hideturtle()
    dot .teleport(0,+399)
    dot.right(90)
    dot.pencolor("white")

    for var in range(0,50):
        dot.forward(10)
        dot.penup()
        dot.forward(10)
        dot.pendown()

    # dot.teleport(-599,0).......#a horizontal dotted line through origin
    # dot.left(90)
    # for var in range(0,80):
    #     dot.forward(10)
    #     dot.penup()
    #     dot.forward(10)
    #     dot.pendown()
    return 


def play():
    """Main functional code of the ball, decides everything like weather\n
    the ball collides or not depending upon the distance between the ball and bars.\n
    updates score depending upon if collision happened or not that too or which side to\n
    increase opposite players score."""
    global ball
    global bar1
    global bar2
    global game_is_on
    global collision_a
    global collision_b
    global score_card_b
    global score_card_a



    which=math.copysign(1,ball.xcor())#to check which side of the axes is the ball on....
     
    if which==1:
        
        d=dist_1()
        if d <= 60:
            motion()
        elif collision_a== False:
            
                ball.home()
                score_card_b += 1
                tur4.clear()
                tur4.write(font=("Arial", 20, "normal"), align="left", arg=f"B:{score_card_b}")
                sleep(1)
        else:
            pass
        
            
    elif which == -1 :
        
        d=dist_2()
        if d <= 60:
                motion()
        elif collision_b==False:
                ball.home()
                score_card_a +=1
                tur3.clear()
                tur3.write(font=("Arial", 20, "normal"), align="left", arg=f"A:{score_card_a}")
                sleep(1)
        else:
                pass    
        collision_b=True
    else:
        raise "play function error"


    

def dist_1():
    """Distance between bar1 and ball."""
    global ball
    global bar2
    global bar1
    return math.sqrt(((ball.ycor())-(bar1.ycor()))**2)
    
def dist_2():
    """Distance between bar2 and ball."""
    global ball
    global bar2
    global bar1
    return math.sqrt((((ball.ycor())-(bar2.ycor()))**2))


def win(score_a,score_b):
    tur5=Turtle()
    tur5.hideturtle()
    tur5.penup()
    tur5.color("white")
    ws=Screen()
    ws.bgcolor("Black")
    ws.screensize(100,100)
    
    
    
    if score_a==10:
       screen.title(f"A WON!!!")
       tur5.write(font=("Arial", 40, "bold"), align="center", arg="GAME OVER\n   'A' WON!!")
    elif score_b==10:
       screen.title(f"B WON!!!")
       tur5.write(font=("Arial", 40, "bold"), align="center", arg="GAME OVER\n   'B' WON!!")
    else:
        pass
    






#********************************************MAIN LOGIC**********************************************#

dotted()
game_is_on=True
messagebox.showinfo("INFO","1.The left side is player B and right side is A.\n"
                    "\n2.Player B is controlled with 'W'-UP and 'S'-DOWN.\n"
                    "\n3.Player A is controlled with 'Up'-UP and 'Down'-DOWN."
                    "\n4.First to 10 points wins.\n"
                    "\n5.The ball resets to origin each time a point is scored.\n"
                    "\n6.Be easy pressing the keys or the ball could start glitching.\n"
                    "\n7.It's just a beginners code so could have unresolved bugs,GO EASY.")
while game_is_on:
    if score_card_a==10 or score_card_b==10:
        game_is_on=False
        ball.home()
        win(score_card_a,score_card_b)
    else:
        ball.speed(2)
        a=random.randint(-299,+299)
        ball.goto(ini_x_cor,a)
        play()
        collision_b=False
        collision_a=False

    

    
    if score_card_a==10 or score_card_b==10:
        game_is_on=False
        ball.home()
        win(score_card_a,score_card_b)
    else:
        b=random.randint(-299,+299)
        ball.goto(-(ini_x_cor),b)
        play()
        collision_b=False
        collision_a=False
#********************************************MAIN LOGIC**********************************************#
screen.exitonclick()
    
    
    
    
   
    

    
    








