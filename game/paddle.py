from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.move_distance = 20



    def go_up(self):
        new_y = self.ycor() + self.move_distance
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - self.move_distance
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    # Paddle movement control
    is_r_paddle_up = False
    is_r_paddle_down = False
    is_l_paddle_up = False
    is_l_paddle_down = False

    def start_moving_up(self):
        self.is_moving_up = True

    def stop_moving_up(self):
        self.is_moving_up = False

    def start_moving_down(self):
        self.is_moving_down = True

    def stop_moving_down(self):
        self.is_moving_down = False

    def move(self):
        if self.is_moving_up:
            self.go_up()
        if self.is_moving_down:
            self.go_down()

