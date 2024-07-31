from turtle import Turtle

class TustleShape(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('Olive')
        self.penup()
        self.setheading(90)
        self.goto(0,-280)

    def turtle_move(self):
        self.forward(20)

    def reset_game(self):
        self.goto(0,-280)