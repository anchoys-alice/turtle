from turtle import *

t1 = Turtle()
t1.color('red')
t1.shape('turtle')
t1.penup()
t1.goto(100,100)
t1.pendown()

t2 = Turtle()
t2.color('orange')
t2.shape('arrow')
t2.penup()
t2.goto(100,-100)
t2.pendown()

t3 = Turtle()
t3.color('#cc6b33')
t3.shape('square')
t3.penup()
t3.goto(-100,100)
t3.pendown()

t4 = Turtle()
t4.color('#cecc31')
t4.shape('classic')
t4.penup()
t4.goto(-100,-100)
t4.pendown()

size = 2
for i in range(30):
    t1.forward(size)
    t1.left(90)
    t2.forward(size)
    t2.left(90)
    t3.forward(size)
    t3.left(90)
    t4.forward(size)
    t4.left(90)
    size += 2
exitonclick()





