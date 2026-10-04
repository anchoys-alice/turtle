from turtle import *

t = Turtle()
t.color('#9228d7')
t.width(5)
t.shape('circle')
t.pendown()
t.speed(6)

def draw(x,y):
    t.goto(x,y)

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def setGreen():
    t.color('#6dd728')
def setViolet():
    t.color('#cc00ff')
def setRed():
    t.color('#eae315')

def stepRight():
    t.goto(t.xcor() +5, t.ycor())
def stepLeft():
    t.goto(t.xcor() -5, t.ycor())
def stepUp():
    t.goto(t.xcor(), t.ycor() +5)
def stepDown():
    t.goto(t.xcor(), t.ycor() -5)

scr = t.getscreen()
scr.listen()
scr.onkey(setGreen, 'g')
scr.onkey(setRed, 'j')
scr.onkey(setViolet, 't')
scr.onkey(stepRight, 'Right')
scr.onkey(stepLeft, 'Left')
scr.onkey(stepUp, 'Up')
scr.onkey(stepDown, 'Down')
scr.onscreenclick(move) 

t.ondrag(draw)
