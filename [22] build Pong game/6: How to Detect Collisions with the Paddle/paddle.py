from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(7.0, 1.0, 1)
        self.penup()
        if position == "left":
            self.setposition(-350,0)
        else:
            self.setposition(350,0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    # def __call__(self):
    #     pass



# paddle = Paddle()

