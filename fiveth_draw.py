# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 00:50:19 2020

@author: Emmanuel
"""

import turtle as t

# Setup window
t.setup(500, 500)

# turtle cursor 
t.shape("turtle")
t.color("green")

# Function

def order():
    order_to_do = t.textinput("Order allowed", "Movements: a, w, s, d - Exit: e")
    
    if order_to_do == "d":
        t.seth(0)
    elif order_to_do == "w":
        t.seth(90)
    elif order_to_do == "a":
        t.seth(180)
    elif order_to_do == "s":
        t.seth(270)
    elif order_to_do == "e":
        t.bye()
    else:
        return # If the user don't type any option, fuction will return
    
    t.forward(50)

while True:
    order()
        

# Close execute
t.done()
t.bye()