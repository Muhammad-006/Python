from turtle import Turtle

FONT = 'center'
ALLIGN = ('Courier', 16, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('WhiteSmoke')
        self.hideturtle()
        self.up()
        self.goto(0,290)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', False, align= FONT, font= ALLIGN)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER.', False, align= FONT, font= ALLIGN)

