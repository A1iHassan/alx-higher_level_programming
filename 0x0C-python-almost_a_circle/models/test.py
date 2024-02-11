#!/usr/bin/python3


import turtle



# Create a screen for the turtle to draw on
screen = turtle.Screen()

# Create a turtle object
t = turtle.Turtle()

# Draw three squares
for color in ["red", "green", "blue"]:
    t.color(color)  # Set the color of the turtle
    for _ in range(4):  # Repeat 4 times to draw each side of the square
        t.forward(100)  # Move the turtle forward by 100 units
        t.right(90)      # Turn the turtle right by 90 degrees
    t.penup()  # Lift the pen up to prevent drawing while moving to the next position
    t.forward(150)  # Move the turtle horizontally to prepare for the next square
    t.pendown()  # Put the pen down to start drawing the next square

# Hide the turtle
t.hideturtle()

# Keep the window open until the user clicks on it
screen.mainloop()

