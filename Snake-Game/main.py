from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(460,640)
screen.bgcolor('black')
screen.title('Snake-Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(fun = snake.up, key = 'Up')
screen.onkey(fun = snake.down, key = 'Down')
screen.onkey(fun = snake.left, key = 'Left')
screen.onkey(fun = snake.right, key = 'Right')


game_on_hay = True
while game_on_hay:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head_of_snake.distance(food) < 20:
        food.refresh()
        score.increase_score()
        snake.extend_snake()

    if (snake.head_of_snake.xcor() > 224.75 or snake.head_of_snake.xcor() < -225 or
            snake.head_of_snake.ycor() > 315 or snake.head_of_snake.ycor() < -315):
        score.reset_game()
        snake.reset_snake()
        time.sleep(2)

    for position in snake.snake_size[1:-1]:
        if snake.head_of_snake.distance(position) < 10:
            score.reset_game()
            snake.reset_snake()
            time.sleep(2)

screen.exitonclick()

