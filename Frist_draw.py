# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:51:45 2020

@author: Emmanuel
"""

# add turtle module
import turtle as t

# Setup window
t.setup(500,500)   

# Here is your code
t.shape("turtle") # add a tirtle
t.color("green") # add color turtle

print("Origen", t.pos())
t.forward(250) # forward turtle
t.left(90) # 90 degrees
t.forward(250)
print("Right upper corner", t.pos())
t.left(90)
t.forward(500)
print("Left upper corner", t.pos())
t.left(90)
t.forward(500)
print("Left lower corner", t.pos())
t.left(90)
t.forward(500)
print("Right lower corner", t.pos())
t.left(90)
t.forward(500)
print("Right upper corner", t.pos())

# close the execute
t.done()
t.bye()

