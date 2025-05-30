from turtle import Turtle, Screen
from paddle  import Paddle
from ball import Ball
import time
from scorboard import Scoreboard
screen = Screen()
screen.bgcolor('black')
screen.setup(width = 800, height = 600)
screen.title('pong')
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
balls = Ball()
score = Scoreboard()



screen.listen()
screen.onkey(fun =right_paddle.go_up, key = 'Up')
screen.onkey(fun =right_paddle.go_down, key = 'Down')
screen.onkey(fun =left_paddle.go_up, key = 'w')
screen.onkey(fun =left_paddle.go_down, key = 's')
game_is_on = True

while game_is_on:
    screen.update()


    time.sleep(0.1)
    balls.move()

    if balls.ycor() > 280 or balls.ycor() < -280:
        balls.bounce_y()

    if balls.distance(right_paddle) < 50 and balls.xcor()  >320:
        balls.bounce_x()


    if balls.distance(left_paddle) <50 and balls.xcor()  <-320:
        balls.bounce_x()

    if balls.xcor() >380:
        balls.reset_position()
        score.l_point()

    if balls.xcor() <-380:
        balls.reset_position()
        score.r_point()












screen.exitonclick()