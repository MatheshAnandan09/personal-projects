import turtle
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import score_board
screen = Screen()
food = Food()
score = score_board()

screen.setup(600,600)
screen.bgcolor('black')
screen.title('snakegame')
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
snake.create_snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        score_board.increase_score(self= score)

    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor()>280 or snake.head.ycor() <-280:

        score_board.reset(self = score)
        snake.reset()
        snake.create_snake()


    for segment in snake.body[1: ]:
        if snake.head.distance(segment) < 10:

            score_board.reset(self=score)
            snake.reset()
            snake.create_snake()












screen.exitonclick()