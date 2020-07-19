# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:39:23 2020

@author: Emmanuel
"""

import turtle as t

# Setup window
t.setup(500, 500)

# turtle cursor 
t.shape("turtle")
t.color("green")

# Function by each action

def right():
    t.seth(0)
    t.forward(20)
    
def left():
    t.seth(180)
    t.forward(20)
    
def up():
    t.seth(90)
    t.forward(20)
    
def down():
    t.seth(270)
    t.forward(20)
    
def exit_to_program():
    t.bye()
        
# Linking each function with a keyboard key
t.onkey(up, "w")
t.onkey(left, "a")
t.onkey(right, "d")
t.onkey(down, "s")
t.onkey(exit_to_program, "e")

# turtle listens the commands
t.listen()

# Close execute
t.done()
t.bye()