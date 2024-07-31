from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
class Snake:

    def __init__(self):
        self.snake_size = []
        self.create_snake()
        self.head_of_snake = self.snake_size[0]
        self.head_of_snake.shape("turtle")

    def create_snake(self):
        for i in START_POSITION:
            self.add_piece(i)

    def add_piece(self, position):
        new_piece = Turtle('square')
        new_piece.color('white')
        self.snake_size.append(new_piece)
        new_piece.up()
        new_piece.goto(position)


    def extend_snake(self):
        self.add_piece(self.snake_size[-1].position())
    def move(self):
        for i in range(len(self.snake_size) - 1, 0, -1):
            x = self.snake_size[i - 1].xcor()
            y = self.snake_size[i - 1].ycor()
            self.snake_size[i].goto(x, y)
        self.head_of_snake.forward(MOVING_DISTANCE)

    def reset_snake(self):
        for piece in self.snake_size:
            piece.goto(1000, 1000)
        self.snake_size.clear()
        self.create_snake()
        self.head_of_snake = self.snake_size[0]
        self.head_of_snake.shape("turtle")

    def up(self):
        if self.head_of_snake.heading() != 270:
            self.head_of_snake.setheading(90)

    def down(self):
        if self.head_of_snake.heading() != 90:
            self.head_of_snake.setheading(270)

    def left(self):
        if self.head_of_snake.heading() != 0:
            self.head_of_snake.setheading(180)

    def right(self):
        if self.head_of_snake.heading() != 180:
            self.head_of_snake.setheading(0)


