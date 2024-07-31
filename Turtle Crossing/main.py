from turtle import Screen
from turtleshape import TustleShape
from cars import Cars
from level import Level
import time

initializer = 1

screen = Screen()
screen.tracer(0)
screen.bgcolor('Gainsboro')
screen.setup(600, 600)

shape = TustleShape()
level_value = Level()
car_shape = Cars()

screen.listen()
screen.onkey(fun = shape.turtle_move, key ='Up')

game_on_hay = True
while game_on_hay:
    time.sleep(car_shape.car_speed)
    screen.update()
    if initializer % 6 == 0:
        car_shape.create_car()
        car_shape.car_move()

    for single_car in car_shape.all_cars:
        if shape.distance(single_car) <= 20:
            level_value.game_over()
            game_on_hay = False

    if shape.ycor() > 280:
        shape.reset_game()
        level_value.increase_level()
        car_shape.car_speed *= 0.9

    initializer += 1


screen.exitonclick()