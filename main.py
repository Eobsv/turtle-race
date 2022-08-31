import random
import turtle

screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle gonna win the race? Enter a color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for turtle_index in range(0, 6):
    tim = turtle.Turtle(shape="turtle")
    tim.penup()
    tim.goto(-230, -100 + 25 * turtle_index)
    tim.color(colors[turtle_index])

screen.exitonclick()
