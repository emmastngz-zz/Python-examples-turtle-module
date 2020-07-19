# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 00:13:42 2020

@author: Emmanuel
"""

"""
    backward --> Go to back
    right ---> Go to right
    penup --> The turtle don't write a line
    pendown --> The turtle write a line
    
    Draw: 
    rectangle
    400 width x 300 length
"""

import turtle as t

# Setup window
t.setup(500, 500)

# turtle cursor 
t.shape("turtle")
t.color("green")

# Draw rectangle
t.penup()
t.forward(200)
t.pendown()
t.left(90)
t.forward(150)
print(t.pos())
t.left(90)
t.forward(400)
print(t.pos())
t.left(90)
t.forward(300)
print(t.pos())
t.left(90)
t.forward(400)
print(t.pos())
t.left(90)
t.forward(150)



# Close execute
t.done()
t.bye()