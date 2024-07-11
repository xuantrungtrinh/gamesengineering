from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)


l_paddle = Paddle("left")
r_paddle = Paddle("right")
# screen.update()
ball = Ball()

# paddle()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

def stop_game(x = 5, y = 3):
    global game_is_on
    game_is_on = False

screen.onclick(stop_game)

while game_is_on:
    time.sleep(0.1) #==> make the ball moves slower. Alternatively, I can also reduce 10 by, like, 9 in the "ball.py" file (but I din't want to).
    screen.update()
    ball.move()

