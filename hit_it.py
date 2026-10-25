from turtle import *
class Sprite(Turtle):
    def __init__(self, x,y, step=10, shape='circle',color='black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x,y)
        self.color(color)
        self.shape(shape)
        self.step = step
    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return Turtle
        else:
            return False
    
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
        
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)

    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    
    def set_move(self,x_start,y_start, x_end,y_end):
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end,y_end))
    
    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end,self.y_end) < self.step:
            self.set_move(self.x_end,self.y_end,self.x_start,self.y_start)


player = Sprite(0, -100, 10, 'circle', 'orange')
print(player.color)
enemy1 = Sprite(210, 10, 15, 'square', 'red')
enemy1.set_move(210,10,-210,10)
enemy2 = Sprite(-210, 50, 15, 'square', 'red')
enemy2.set_move(-210,50,210,50)
enemy3 = Sprite(210,80,100, 'circle', 'yellow')
enemy3.set_move(210,80,210,-80)
purpose = Sprite(0,180,0, 'triangle', 'green')

scr = player.getscreen()
scr.listen()

scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')

total_score = 0

while total_score < 3:
    enemy1.make_step()
    enemy2.make_step()
    enemy3.make_step()
    if player.is_collide(purpose):
        player.goto(0, -100)
        total_score += 1
    if player.is_collide(enemy1) or player.is_collide(enemy2):
        purpose.hideturtle()
        enemy1.hideturtle()
        enemy2.hideturtle()
        player.goto(-50,0)
        player.write('Поражение', font = ('Arial', 20, 'normal'))
        player.hideturtle()
        purpose.hideturtle()
        enemy3.hideturtle()
        break

if total_score == 3:
    enemy1.hideturtle()
    enemy2.hideturtle()
    player.goto(-50,0)
    player.write('Победа!', font = ('Arial', 20, 'normal'))
    player.hideturtle()
    purpose.hideturtle()
    enemy3.hideturtle()
