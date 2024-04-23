from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.directions = [0, 180, 90, 270]
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.setpos(self.pos()[0] + self.x_move, self.pos()[1] + self.y_move)

    def ball_reset(self):
        self.setpos(0, 0)
        self.setheading(random.choice(self.directions[:2]))

    def bounce_y(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1

    def bounce_x(self, position):
        if self.xcor() > (position[0] - 20) or self.xcor() < -(position[0] - 20):
            self.x_move *= -1

    def increase_speed(self):
        self.x_move *= 1.2
        self.y_move *= 1.2
