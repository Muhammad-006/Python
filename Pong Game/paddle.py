from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, locate):
        super().__init__()
        self.shape('square')
        self.color('Gainsboro')
        self.speed('fastest')
        self.shapesize(5, 0.5)
        self.penup()
        self.goto(locate)


    def up(self):
            x = self.xcor()
            y = self.ycor() + 40
            self.goto(x, y)

    def down(self):
            x = self.xcor()
            y = self.ycor() - 40
            self.goto(x, y)





