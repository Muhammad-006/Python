from turtle import Screen
from paddle import Paddle
from pongball import PongBall
from scoreboard import ScoreBoard
import time


STARTING_POSITIONS = [(350, 0), (-350, 0), (380, 188)]

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 400)
screen.title('PONG')
screen.tracer(0)

right_paddle = Paddle(STARTING_POSITIONS[0])
left_paddle = Paddle(STARTING_POSITIONS[1])
pong_ball = PongBall()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=right_paddle.up, key='Up')
screen.onkey(fun=right_paddle.down, key='Down')
screen.onkey(fun=left_paddle.up, key='w')
screen.onkey(fun=left_paddle.down, key='s')

game_on_hay = True
while game_on_hay:
    time.sleep(pong_ball.taken_time)
    screen.update()
    pong_ball.move()
    if pong_ball.ycor() > 180 or pong_ball.ycor() < -180:
        pong_ball.bounce_back_in_y_axis()

    if pong_ball.xcor() > 350 or pong_ball.xcor() < -350:
        pass
    elif right_paddle.distance(pong_ball) <= 60 or left_paddle.distance(pong_ball) <= 60:
        if pong_ball.xcor() == right_paddle.xcor() - 20 or pong_ball.xcor()  == left_paddle.xcor() + 20:
            pong_ball.bounce_back_in_x_axis()

    if pong_ball.xcor() > 410:
        score.increase_left_score()
        pong_ball.reset_position()

    if pong_ball.xcor() < -410:
        score.increase_right_score()
        pong_ball.reset_position()

    if score.right_score == 20 or score.left_score == 20:
        if score.right_score >= 19 and score.left_score <= 19:
            score.give_chance()
        elif score.right_score == 19 or score.left_score == 19:
            score.game_point()
        else:
            score.game_over()
            game_on_hay = False

screen.exitonclick()