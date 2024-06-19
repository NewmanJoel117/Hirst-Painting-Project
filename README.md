# Hirst Multi-Colors Dot Painting with Turtle

This project creates a dot painting inspired by artist Damien Hirst using Python's Turtle graphics module. The script randomly selects colors from a predefined list and places dots in a grid pattern.

## Project Description

The script utilizes the `turtle` module to draw a series of colored dots on the screen. Colors are randomly chosen from a list of RGB values. The turtle moves in a grid-like pattern to create the painting. 

## Prerequisites

- Python 3.x
- `turtle` module (usually included with Python)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/hirst-dot-painting.git
    cd hirst-dot-painting
    ```

2. Run the script:
    ```sh
    python hirst_dot_painting.py
    ```

## Usage

Simply run the script, and a window will open displaying the dot painting being created in real time. The painting consists of 100 dots arranged in a grid.

## Code Explanation

Here's a brief overview of the script:

```python
import turtle as turtle_module
import random

# Set up turtle
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')

# List of RGB colors
color_list = [
    (247, 236, 37), (240, 244, 251), (239, 231, 3), (36, 216, 77), 
    (223, 159, 61), (39, 79, 185), (28, 39, 159), (210, 73, 16), 
    (17, 151, 18), (239, 39, 152), (65, 9, 27), (188, 14, 9), 
    (216, 25, 127), (218, 140, 198), (223, 161, 7), (59, 12, 7), 
    (67, 202, 227), (10, 96, 60), (84, 80, 212), (17, 19, 52), 
    (237, 157, 218), (106, 232, 195), (99, 205, 136), (212, 84, 58), 
    (8, 222, 235), (236, 171, 161)
]

# Position the turtle
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# Draw dots
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

# Exit on click
screen = turtle_module.Screen()
screen.exitonclick()
```

## Color Extraction

To extract colors from an image, the `colorgram` library was used. The extracted colors were converted to RGB format and saved in `color_list`.

## Author

Onyedika Joel Chukwuka
