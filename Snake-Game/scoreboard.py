from turtle import Turtle

FONT = ('Courier', 16, 'normal')
ALLIGN = 'center'

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('WhiteSmoke')
        self.hideturtle()
        self.up()
        self.goto(0,290)
        self.score = 0
        with open('highestscore.txt', mode='r') as file:
            self.highest_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} | Highest score: {self.highest_score}', False,
                   align= ALLIGN, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_game(self):
        if self.highest_score < self.score:
            self.highest_score = self.score
            with open('highestscore.txt', mode='w') as file:
                file.write(f'{self.highest_score}')
        self.score = 0
        self.goto(0, 290)
        self.update_scoreboard()
