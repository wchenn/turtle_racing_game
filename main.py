from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "blue", "green", "purple", "yellow"]

y_pos = [-60, -40, -20, 0, 20, 40]
all_turtles = []
for turt_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x= -230, y = y_pos [turt_index])
    new_turtle.color(colors[turt_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! the {winning_color} turtle is the winner")
            else:
                print(f"you've lost! the {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)

screen.exitonclick()
