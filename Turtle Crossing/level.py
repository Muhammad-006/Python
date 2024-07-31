from turtle import Turtle

FONT =('Courier', 18, 'normal')
ALIGN = 'left'

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('DimGray')
        self.up()
        self.hideturtle()
        self.write_level()

    def write_level(self):
        self.clear()
        self.goto(-270, 260)
        self.write(f'Level: {self.level}', font= FONT, align= ALIGN)

    def increase_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.color('Crimson')
        self.goto(0, 0)
        self.write(f'GAME OVER', font= FONT, align= 'center')
