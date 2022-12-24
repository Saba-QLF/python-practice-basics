import random
import turtle

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet",
                            prompt="Which turtles will win the game? Enter a color: ")


def make_turtle(color, y):
    the_turtle = turtle.Turtle(shape="turtle")
    the_turtle.color(color)
    the_turtle.penup()
    the_turtle.goto(x=-230, y=y)
    return the_turtle


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []
for i in range(6):
    new_turtle = make_turtle(colors[i], y_positions[i])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for one_turtle in turtles:
        if one_turtle.xcor() > 230:
            winning_color = one_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")
            is_race_on = False
            break
        rand_distance = random.randint(0, 10)
        one_turtle.forward(rand_distance)

screen.exitonclick()
