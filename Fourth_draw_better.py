# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 01:34:09 2020

@author: Emmanuel
"""

import turtle as t

# Setup window
t.setup(500, 500)

# turtle cursor 
t.shape("turtle")
t.color("green")

# Function

def regular_polygon(px, py, radius, sides):
    # Don't allow to the turtle draw
    t.penup()

    # We calculate the angle
    angle = 360 / sides
    print(angle)
    
     # A list to save the vertices values
    vertices = []
    
    for i in range(sides):
        t.goto(px,py)   # Go to center
        t.seth(angle*i+1) # Draw the radios
        t.forward(radius)
        vertices.append(t.pos()) # To add to list
        
    # to go to last vertice
    t.goto(vertices[-1])
    
    # Allow to the turtle draw
    t.pendown()
    
    # turtle go to each vertice
    for v in vertices:
        t.goto(v)
        
        
regular_polygon(0, 0,100, 7)


# Close execute
t.done()
t.bye()