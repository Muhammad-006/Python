from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.up()
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        self.refresh()

    def refresh (self):
        x = random.randint(-210, 210)
        y = random.randint(-300, 300)
        self.goto(x, y)



