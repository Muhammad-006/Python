from turtle import Turtle

FONT = ('Courier', 16, 'normal')
ALLIGN = 'center'
class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('Crimson')
        self.speed('fastest')
        self.penup()
        self.x_position = 10
        self.y_position = 10
        self.taken_time = 0.1


    def move(self):
        x = self.xcor() + self.x_position
        y = self.ycor() + self.y_position
        self.goto(x, y)

    def bounce_back_in_y_axis(self):
        self.y_position *= -1

    def bounce_back_in_x_axis(self):
        self.x_position *= -1
        self.taken_time *= 0.9

    def reset_position(self):
        self.taken_time = 0.1
        self.goto(0, 0)
        self.bounce_back_in_x_axis()


