import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

game_running = True
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")

paddle_left = Paddle(-350, 0)
paddle_right = Paddle(350, 0)

ball = Ball()
scoreboard = Scoreboard()

screen.tracer(0)
screen.listen()
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

while (game_running):
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if abs(ball.ycor()) > 280:
        ball.bounce_wall()

    if (ball.distance(paddle_right) < 50 or ball.distance(paddle_left) < 50) and abs(ball.xcor()) > 320:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.update_score("left_score")

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.update_score("right_score")

    if scoreboard.left_score == 10 or scoreboard.right_score == 10:
        scoreboard.end_game()
        game_running = False

screen.exitonclick()
