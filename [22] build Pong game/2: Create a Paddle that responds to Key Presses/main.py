from turtle import Screen, Turtle
from paddle import Paddle


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)


l_paddle = Paddle("left")
r_paddle = Paddle("right")
# screen.update()


# paddle()


def r_go_up():
    new_y = r_paddle.ycor() + 20
    r_paddle.goto(r_paddle.xcor(), new_y)

    # screen.update()

def r_go_down():
    new_y = r_paddle.ycor() - 20
    r_paddle.goto(r_paddle.xcor(), new_y)

    # screen.update()

def l_go_up():
    new_y = l_paddle.ycor() + 20
    l_paddle.goto(l_paddle.xcor(), new_y)

def l_go_down():
    new_y = l_paddle.ycor() - 20
    l_paddle.goto(l_paddle.xcor(), new_y)

screen.listen()
screen.onkey(r_go_up, "Up")
screen.onkey(l_go_up, "w")
screen.onkey(r_go_down, "Down")
screen.onkey(l_go_down, "s")

game_is_on = True

def stop_game(x = 5, y = 3):
    global game_is_on
    game_is_on = False

screen.onclick(stop_game)

while game_is_on:
    screen.update()

