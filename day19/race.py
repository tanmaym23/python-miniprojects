from turtle import Turtle,Screen

screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="make your bet",prompt="choose your colour")
print(user_bet)
colours=["red", "green", "blue", "purple"]

t=Turtle(shape="turtle")
t.penup()
t.goto(x=-230,y=-150)
t.color("red")

r=Turtle(shape="turtle")
r.penup()
r.goto(x=-230,y=-50)
r.color("green")

l=Turtle("turtle")
l.penup()
l.goto(x=-230,y=50)
l.color("blue")

a=Turtle(shape="turtle")
a.penup()
a.goto(x=-230,y=150)
a.color=("purple")

screen.exitonclick()
