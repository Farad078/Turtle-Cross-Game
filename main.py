from turtle import Turtle,Screen
from player import Player
from traffic import Traffic
from scoreboard import ScoreBoard,Message

import random
import time

screen = Screen()
screen.title(" Turtle Crossing")
screen.setup(width=600, height=600)

screen.tracer(0)
player = Player()
score = ScoreBoard()
msg = Message()

trafik = []
for k in range(0, 5):
    traffic = Traffic()
    trafik.append(traffic)


screen.listen()


screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(player.move_left, "Left")
# screen.onkeypress(traffic.travel, "a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    for cars in trafik:
        cars.travel()
        cars.generate()
        if cars.distance(player) < 33:
            msg.l_output()
            game_is_on = False
    if player.ycor() >= 280:
        score.count()
        msg.w_output()
        player.refresh()











screen.exitonclick()