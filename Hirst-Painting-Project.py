import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
color_list = [(247, 236, 37), (240, 244, 251),
              (239, 231, 3), (36, 216, 77), (223, 159, 61), (39, 79, 185), (28, 39, 159), (210, 73, 16), (17, 151, 18),
              (239, 39, 152), (65, 9, 27), (188, 14, 9), (216, 25, 127), (218, 140, 198), (223, 161, 7), (59, 12, 7),
              (67, 202, 227), (10, 96, 60), (84, 80, 212), (17, 19, 52), (237, 157, 218), (106, 232, 195),
              (99, 205, 136), (212, 84, 58), (8, 222, 235), (236, 171, 161)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

"""Color extraction
import colorgram"""

'''rgb_colors = []
colors = colorgram.extract('Hirst Multi-Colors.jpeg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)'''
