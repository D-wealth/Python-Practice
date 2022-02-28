# DISCORD.GG / SENTDEX
# TURTLE IN PYTHON 
import turtle
my_turtle = turtle.Turtle()

# DEFINING A SQUARE 
def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)

length = 100
angle = 90

for i in range(100):
    square(length, angle)
    my_turtle.right(11)