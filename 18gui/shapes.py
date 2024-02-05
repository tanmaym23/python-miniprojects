from turtle import Turtle, Screen 

trtl =Turtle()

def shape_(side):
    angle=360/side
    for _ in range(side):
        trtl.forward(100)
        trtl.right(angle)

for n in range(3,11):
    shape_(n)

screen=Screen()
screen.exitonclick()