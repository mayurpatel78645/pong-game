from turtle import Turtle


class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.setheading(270)
        self.pendown()
        self.forward(500)
