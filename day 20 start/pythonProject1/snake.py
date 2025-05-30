from turtle import Turtle, Screen
BODY_POSITION = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

MOVE = 20

class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in BODY_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        turtles = Turtle()
        turtles.shape('square')
        turtles.color('white')
        turtles.penup()
        turtles.goto(position)
        self.body.append(turtles)

    def reset(self):
        for san in self.body:
            san.goto(1000,1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]
    def extend(self):
        self.add_segment(self.body[-1].position())



    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def  down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




