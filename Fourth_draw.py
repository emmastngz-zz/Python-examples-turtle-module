# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 01:02:13 2020

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
    t.penup()
    t.goto(px, py - radius)
    t.pendown()
    t.circle(radius)
    
    angle = 360 / sides
    print(angle)
    
    vertices = [] # A list to save the vertices values
    
    for i in range(sides):
        t.penup()
        t.goto(px,py)   # Go to center
        t.pendown()
        
        t.seth(angle*i+1) # Draw the radios
        t.forward(radius)
        vertices.append(t.pos()) # To add to list
        
    # to go to first vertice
    t.penup()
    t.goto(vertices[0])
    t.pendown()
    
    # turtle go to each vertice
    for v in vertices:
        t.goto(v)
        
    # for the last vertice
    t.goto(vertices[0])
        
regular_polygon(0, 0,100, 7)


# Close execute
t.done()
t.bye()