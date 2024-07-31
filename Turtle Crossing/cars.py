import turtle
from turtle import Turtle
import random

turtle.colormode(255)

class Cars:
    def __init__(self):
        self.all_cars = []
        self.create_car()
        self.car_speed = 0.1

    def create_car(self):
        y = random.randint(-250, 250)
        new_piece = Turtle('square')
        new_piece.shapesize(1, 2)
        new_piece.color(self.generate_color())
        new_piece.penup()
        new_piece.setheading(180)
        new_piece.goto(300, y)
        self.all_cars.append(new_piece)

    def generate_color(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return r, g, b

    def car_move(self):
        for car in self.all_cars:
            car.forward(20)

    def increase_car_speed(self):
        self.car_speed *= 0.5








