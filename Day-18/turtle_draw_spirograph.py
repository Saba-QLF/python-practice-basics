import turtle
import random

the_turtle = turtle.Turtle()
the_turtle.shape("turtle")
turtle.colormode(255)
# the_turtle.pensize(10)
the_turtle.speed(0)


def draw_spirograph(size_of_gap):
    for i in range(360 // size_of_gap):
        random_color = (random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255))
        the_turtle.color(random_color)
        the_turtle.circle(100)
        the_turtle.setheading(the_turtle.heading() + size_of_gap)

draw_spirograph(10)

screen = turtle.Screen()
screen.exitonclick()
