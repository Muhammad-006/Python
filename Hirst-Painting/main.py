import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
import colorgram

color = [(236, 244, 250), (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132),
         (110, 179, 216), (217, 163, 101), (27, 105, 168),(35, 186, 109), (19, 29, 168), (13, 23, 66)]


Tom = Turtle()
Tom.speed('fastest')
Tom.up()
Tom.setposition(-430, -260)
Tom.down()
for _ in range (18):
    for _ in range (40):
        if _ % 2 == 0:
            Tom.up()
            Tom.setheading(0)
            Tom.forward(40)
            Tom.down()
        else:
            Tom.color(random.choice(color))
            Tom.begin_fill()
            Tom.circle(10)
            Tom.end_fill()
    Tom.up()
    Tom.setposition(-430, Tom.ycor() + 30)
    Tom.down()

screen = Screen()
screen.exitonclick()




