import turtle
the_turtle = turtle.Turtle()
the_turtle.shape("turtle")
the_turtle.color("orange2")
for i in range(50):
    the_turtle.penup()
    the_turtle.forward(10)
    the_turtle.pendown()
    the_turtle.forward(10)
screen = turtle.Screen()
screen.exitonclick()