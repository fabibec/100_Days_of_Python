import random
from turtle import Turtle, Screen
import random

is_race_on = False
user_bet = ""
winner = ""
screen = Screen()
screen.setup(width=500, height=400, startx=0, starty=0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

start_pos = -150
increment_pos = 300 / 7

for i in range(6):
    globals()['turtle%s' % i] = Turtle(shape="turtle")
    start_pos += increment_pos
    globals()['turtle%s' % i].color(colors[i])
    globals()['turtle%s' % i].pu()
    globals()['turtle%s' % i].goto(x=-230, y=start_pos)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in range(6):
        globals()['turtle%s' % i].forward(random.randint(0, 10))
        if globals()['turtle%s' % i].xcor() >= 250:
            winner = globals()['turtle%s' % i].pencolor()
            is_race_on = False

if winner == user_bet:
    print(f"You won, the winner was the {winner} turtle!")
else:
    print(f"You lost, the winner was the {winner} turtle!")

screen.exitonclick()





