Ejemplos_sep2825.rst

import turtle

# Create a Screen object
screen = turtle.Screen()

# Set the window size to 800 pixels wide and 600 pixels high
screen.setup(width=800, height=600)

# Alternatively, set the size as a fraction of the screen's dimensions (e.g., 50% width, 75% height)
# screen.setup(width=0.5, height=0.75)

# Create a Turtle object and draw
t = turtle.Turtle()
t.forward(100)

# Keep the window open until closed manually
turtle.done()


