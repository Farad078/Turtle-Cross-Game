from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.refresh()
        self.walk = 10

    def refresh(self):
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)

    def move_up(self):
        new_y = self.ycor()
        self.goto(self.xcor(), new_y + self.walk)

    def move_dwn(self):
        new_y = self.ycor()
        self.goto(self.xcor(), new_y - self.walk)

    def move_right(self):
        new_x = self.xcor()
        self.goto(new_x + self.walk, self.ycor())

    def move_left(self):
        new_x = self.xcor()
        self.goto(new_x - self.walk, self.ycor())
