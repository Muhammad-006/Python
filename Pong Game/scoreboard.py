from turtle import Turtle

FONT = ('Courier', 40, 'bold')
ALLIGN = 'center'


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.color('Gainsboro')
        self.left_score = 0
        self.right_score = 0
        self.write_score()
    def write_score(self):
        self.clear()
        self.goto(-70, 140)
        self.write(f'{self.left_score}', font=FONT, align=ALLIGN)
        self.goto(70, 140)
        self.write(f'{self.right_score}', font=FONT, align=ALLIGN)
    def increase_left_score(self):
        self.left_score += 1
        self.write_score()

    def increase_right_score(self):
        self.right_score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.color('Crimson')
        self.write('GAME OVER', align= ALLIGN, font= ('Courier', 18, 'bold'))

    def give_chance(self):
        self.right_score = 17
        self.left_score = 17
        self.goto(0, 0)
        self.color('Crimson')
        self.write('Score leveled', align=ALLIGN, font=('Courier', 18, 'bold'))
        self.write_score()

    def game_point(self):
        self.goto(0, 0)
        self.color('Crimson')
        self.write('Score leveled', align=ALLIGN, font=('Courier', 18, 'bold'))
