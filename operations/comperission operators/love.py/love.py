import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Love")

t = turtle.Turtle()
t.speed(0)
t.color("red")
t.pensize(3)

def heart(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

heart(0, 0)

t.hideturtle()
turtle.done()