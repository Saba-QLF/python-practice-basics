import turtle
import random

the_turtle = turtle.Turtle()
the_turtle.shape("turtle")
turtle.colormode(255)
# colors = ["maroon", "dark green", "dark orange",
#          "medium violet red", "indigo", "gold",
#          "medium spring green", "navy", "dark cyan"]
directions = [0, 90, 180, 270]
the_turtle.pensize(10)
the_turtle.speed(0)
for step in range(500):
    random_color = (random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255))
    the_turtle.color(random_color)
    the_turtle.forward(30)
    the_turtle.setheading(random.choice(directions))
    # the_turtle.setheading(random.randint(0, 360))

screen = turtle.Screen()
screen.exitonclick()
