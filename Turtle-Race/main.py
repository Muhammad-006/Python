from turtle import Turtle,Screen,getscreen
import random


ts = getscreen()
ts.bgcolor("LightCyan")
screen = Screen()


var = screen.textinput('Make a bet', 'Who will win the race?')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
speeds = [0,1,10,6,3]
tur = []
y = 60 * 4.5


for i in range (7):
    color = random.choice(colors)
    tur.append(color)
    tur[i] = Turtle()
    colors.remove(color)
    tur[i].color(color)
    tur[i].shape('turtle')
    tur[i].shapesize(1.5)
    y = y - 60
    tur[i].penup()
    tur[i].setposition(-620, y)

highest = 0
while highest < 620:
    for i in range(7):
        name = tur[i]
        test = random.choice(speeds)
        name.speed(test)
    for i in range(7):
        steps = random.randint(5, 40)
        name = tur[i]
        name.forward(steps)
        position = list(name.position())
        if position[0] >= 620:
            break
    for i in range(7):
        name = tur[i]
        if highest <= name.xcor():
            highest = name.xcor()

for i in range (7):
    name = tur[i]
    if name.xcor() == highest:
        color = list(name.color())
        if var == color[0]:
            print(f'You were right! {color[0]} has won.')
        else:
            print(f'Oh! {color[0]} has won.')

screen.exitonclick()