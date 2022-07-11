from turtle import Turtle
import time


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.score = 0
        self.goto(0, 240)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Level: {self.score}", align='Center', font=('Arial', 20, 'normal'))


    def count(self):
        self.clear()
        self.score += 1
        self.update()

class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()


    def w_output(self):
        self.clear()
        text = "You Win!!"
        self.write(text, align='Center', font=("Arial", 24, 'normal'))
        time.sleep(1)
        self.clear()

    def l_output(self):
        self.clear()
        text = "You Lose!!"
        self.write(text, align='Center', font=("Arial", 24, 'normal'))
        time.sleep(1)
        self.clear()
