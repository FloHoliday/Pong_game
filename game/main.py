from turtle import Screen
from game.paddle import Paddle
from game.ball import Ball
from game.scoreboard import Scoreboard
import time

def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("PONG")
    screen.tracer(0)

    r_paddle = Paddle((350, 0), "green")
    l_paddle = Paddle((-350, 0), "red")
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Collision detection and score update code here
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.bounce_y()

        # Detect collision paddles
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (
                ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        # Detect right paddle miss
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        # Detect left paddle miss
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()

    screen.exitonclick()


if __name__ == "__main__":
    main()
