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
    time.sleep(0.045)  #==> make the ball moves slower: pause the loop for a short time during each iteration. ==> get our while loop to sleep for a little bit in between each of the updates. ==> Also, I can think of it as getting the ball to move on every refresh of the screen.
        #==> Alternatively, I can also reduce 10 by, like, 9 in the "ball.py" file (but I din't want to).
    screen.update()
    ball.move()

    # Detect collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        # ==> So this will take a little bit of thinking to get your head around it. ==> The best way to really understand this is to print out the values of the new_y and also of the y_move and also after you've modified the move in the bounce, look at those numbers and you'll eventually be able to understand what's actually happening to the position of the ball.
            # ==> But effectively, all that we're doing is we're defining an amount that the ball is going to move by in the X and the Y axis. We're adding that amount to the X and Y coordinates in order to move the ball. And when the ball needs to bounce off the top and bottom walls, we reverse the y_move number so that we get it to subtract instead of add. And that moves it in the opposite direction.

    # Detect collision with r_paddle:
    if ball.distance(r_paddle) < 50 and 330 < ball.xcor() < 350 or ball.distance(l_paddle) < 50 and -350 < ball.xcor() < -330:
        # print("Make contact")
        ball.bounce_x()



