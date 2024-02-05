from turtle import Turtle ,Screen
trtl=Turtle()
trtl.penup()
trtl.hideturtle()
trtl.speed(0)

trtl.setheading(225)
trtl.forward(300)
trtl.setheading(0)

for dots in range(1,101):
    trtl.dot (20)
    trtl.forward(50)

    if dots%10==0:
        trtl.setheading(90)
        trtl.forward(50)
        trtl.setheading(180)
        trtl.forward(500)
        trtl.setheading(0)
        
screen=Screen()
screen.exitonclick()
