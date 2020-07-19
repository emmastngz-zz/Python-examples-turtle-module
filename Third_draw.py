# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 00:47:34 2020

@author: Emmanuel
"""

import turtle as t

# Setup window
t.setup(500, 500)

# turtle cursor 
t.shape("turtle")
t.color("green")

# Function

def rectangle(px, py, width, length):
    
    t.penup()
    t.goto(px + width/2, py + length/2)
    t.seth(180)
    t.pendown()
    t.forward(width)
    t.seth(270)
    t.forward(length)
    t.seth(0)
    t.forward(width)
    t.seth(90)
    t.forward(length)
    
    

rectangle(0, 0, 400, 300)
rectangle(0, 0, 300, 200)
rectangle(0, 0, 200, 100)
rectangle(0, 0, 50, 50)




# Close execute
t.done()
t.bye()