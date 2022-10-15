import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move(20)

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        score.reset_score()
        snake.reset_position()

    for body_el in snake.snake_body[1:]:
        if body_el.position() == snake.head.position():
            score.reset_score()
            snake.reset_position()

screen.exitonclick()
