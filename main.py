from turtle import Turtle, Screen
import random

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# timmy_the_turtle = Turtle("turtle")
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
# timmy_the_turtle.penup()
# timmy_the_turtle.goto(x=-230, y=-100)

turtle_list = []
for i in range(len(colors)):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    y = -70 + (30 * i)
    new_turtle.goto(x=-230, y=y)
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(
                    f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False
            continue

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
