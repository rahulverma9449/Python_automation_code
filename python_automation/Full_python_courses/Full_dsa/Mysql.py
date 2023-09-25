import turtle
import time

colors = ["red", "orange","blue", "yellow", "purple", "violet", "green"]


t = turtle.Pen()

t.speed(1000)

turtle.bgcolor("black")

for i in range(200):
    t.pencolor(colors[i%6])
    t.width(i/100 + 1)
    t.forward(i)
    t.left(59)

turtle.done()