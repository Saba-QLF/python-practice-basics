# import colorgram
import random
import turtle

# rgb_colors = []
# colors = colorgram.extract("damien-hirst-spot-painting-for-sale.jpg", 30)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

colors = [(250, 246, 243), (248, 245, 246), (212, 154, 97), (239, 246, 243), (52, 108, 132), (178, 78, 33),
          (198, 143, 34), (123, 80, 97), (235, 240, 244), (116, 155, 171), (124, 175, 158), (228, 197, 129),
          (194, 85, 105), (54, 38, 20), (12, 51, 65), (189, 123, 142), (54, 120, 115), (41, 169, 126), (167, 21, 31),
          (225, 94, 78), (4, 30, 28), (39, 32, 34), (243, 163, 159), (81, 148, 168), (164, 27, 22), (239, 163, 167),
          (104, 123, 159), (164, 209, 193), (21, 81, 93), (29, 85, 81)]

the_turtle = turtle.Turtle()
the_turtle.shape("turtle")
turtle.colormode(255)
the_turtle.hideturtle()
the_turtle.speed(0)
the_turtle.setheading(225)
the_turtle.penup()
the_turtle.forward(300)
the_turtle.setheading(0)
number_of_dots = 100

for i in range(1, number_of_dots + 1):
    the_turtle.dot(20, random.choice(colors))
    the_turtle.forward(50)

    if i % 10 == 0:
        the_turtle.setheading(90)
        the_turtle.forward(50)
        the_turtle.setheading(180)
        the_turtle.forward(500)
        the_turtle.setheading(0)

screen = turtle.Screen()
screen.exitonclick()