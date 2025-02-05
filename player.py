from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape('turtle')
        self.color('black')
        self.finishLine = FINISH_LINE_Y

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        new_x = self.xcor()
        self.goto(new_x, new_y)

    def reposition(self):
        self.goto(STARTING_POSITION)