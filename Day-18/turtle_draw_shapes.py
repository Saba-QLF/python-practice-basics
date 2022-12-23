import turtle
the_turtle = turtle.Turtle()
the_turtle.shape("turtle")
colors = ["maroon", "firebrick", "crimson", "tomato",
          "salmon",  "light pink", "peach puff", "misty rose"]
for side in range(3,11):
    angle = 360/side
    the_turtle.color(colors[(side-3)])
    for i in range(side):
        the_turtle.forward(100)
        the_turtle.right(angle)


screen = turtle.Screen()
screen.exitonclick()