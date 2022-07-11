from turtle import Turtle
import random

COLOR = ["green", "black", "yellow", "magenta", "cyan", "blue", "indigo", "violet", "orange", "pink", "brown", "red",
         "purple"]

POSITION_Y = []
for k in range(-200, 200, 20):
    POSITION_Y.append(k)

POSITION_X = []
for i in range(330, 730, 20):
    POSITION_X.append(i)


class Traffic(Turtle):
    def __init__(self):
        super().__init__()
        self.generate_car()
        self.drive = 5

    def travel(self):
        new_x = self.xcor() - self.drive
        self.goto(new_x, self.ycor())

    def generate_car(self):
        for _ in range(1, 5):
            j = random.choice(range(0, 20, 5))
            col = random.choice(range(0, 12))
            self.shape("square")
            self.color(COLOR[col])
            self.shapesize(stretch_wid=1, stretch_len=3)
            self.penup()
            self.goto(POSITION_X[j], POSITION_Y[j])

    def generate(self):
        if self.xcor() < -330:
            self.generate_car()


