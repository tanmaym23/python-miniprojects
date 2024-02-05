from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")
screen.tracer(0)

rpaddle=Paddle((350,0))
lpaddle=Paddle((-350,0)) 
# paddle=Paddle((100,100)) 
ball=Ball()

screen.listen()
screen.onkey(rpaddle.go_up, "Up")
screen.onkey(rpaddle.go_down, "Down")
screen.onkey(lpaddle.go_up, "w")
screen.onkey(lpaddle.go_down, "s")

game_ison=True
while game_ison==True:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()