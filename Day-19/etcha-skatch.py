import turtle
the_turtle = turtle.Turtle()
screen = turtle.Screen()
the_turtle.speed(0)


def move_forwards():
    the_turtle.forward(10)


def move_backwards():
    the_turtle.backward(10)


def turn_left():
    new_heading = the_turtle.heading() + 10
    the_turtle.setheading(new_heading)


def turn_right():
    new_heading = the_turtle.heading() - 10
    the_turtle.setheading(new_heading)


def clear():
    the_turtle.clear()
    the_turtle.penup()
    the_turtle.home()
    the_turtle.pendown()

    
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
