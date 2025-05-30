from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width =  500, height= 400)
user_input = screen.textinput(title = 'Make a bet', prompt= 'Which color turtle will win the race')

name = ['tim', 'tom', 'timmy', 'tam', 'timmi', 'ben']
colors = ['blue', 'red', 'black', 'green', 'yellow', 'orange']
position_coordinates = [(-250, 200), (-250, 130), (-250, 60), (-250,-10), (-250,-80 ), (-250, -150)]
comp = []

for competitors in name:
    competitors = Turtle()
    comp.append(competitors)
for i in range(6):
    comp[i].penup()
    comp[i].shape('turtle')
    comp[i].color(colors[i])

for i in range(6):
    comp[i].goto(position_coordinates[i])
if user_input :
    is_race_on = True
while is_race_on:

    for i in range(6):
        rand_distance = random.randint(0,10)
        comp[i].forward(rand_distance)
        if comp[i].xcor() >230:
            is_race_on = False
            winning_color = comp[i].pencolor()
            if winning_color == user_input:
                print('you won')
            else:
                print('you lose')






#
































screen.exitonclick()