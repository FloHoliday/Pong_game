from turtle import Screen
from game.paddle import Paddle
from game.ball import Ball
from game.scoreboard import Scoreboard
import time

def run_game():
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

    screen.exitonclick()

if __name__ == "__main__":
    run_game()
