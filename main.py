import re
from shutil import move
import turtle
from utils.snake import Snake
from utils.food import *
from utils.scoreboard import *
import time
import os
import sys


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head_position()[0] < -300 or snake.head_position()[0] > 300 or snake.head_position()[1] < -300 or snake.head_position()[1] > 300:
        scoreboard.game_over()
        game_is_on = False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    if snake.head.distance(food) < 15:
        snake.extend()
        food.new_position()
        scoreboard.increace_score()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


screen.exitonclick()
