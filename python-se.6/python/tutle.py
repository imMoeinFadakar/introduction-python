import turtle
import tkinter
import time

turtle.bgcolor("gray")
lineMaker = turtle.Turtle()

number = 3
forward_number = 60

while  number < 11:

    #step1 : find rotate degree for any shape
    degree_of_shapes = 360 / number
    minus_the_180deg = 180 - degree_of_shapes
    last_needed_degree = degree_of_shapes + (minus_the_180deg / 2)
    lineMaker.color("black")
    lineMaker.forward(10)
    lineMaker.left(last_needed_degree)

    #step2: start moving into boarders:

    for x in range(number):
        lineMaker.forward(forward_number)
        if x != number - 1:
            lineMaker.left(degree_of_shapes)
        else:
            lineMaker.right(minus_the_180deg / 2)
            forward_number += 3

    number += 1 # moving to the next shape



turtle.done()

time.sleep(6)

