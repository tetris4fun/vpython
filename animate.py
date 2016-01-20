# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 23:58:53 2016

@author: piotr
"""

from visual import *

ball=sphere(pos=(-2,0.1, 0), radius=0.1, color=color.red)
floor=box(pos=(0,0,0), size=(7,0.05,1),color=color.green)

#set up initial conditions
ball.velocity=vector(5,5,0)
ball.mass=0.25
ball.p=ball.velocity*ball.mass
g=vector(0,-9.8,0)
Fnet=g*ball.mass
dt = 0.001
t = 0


while True:
    rate(300)
    ball.pos=ball.pos + (ball.p/ball.mass)*dt
    ball.p = ball.p +Fnet*dt
    t = t + dt
    if ball.pos.y < (floor.pos.y + ball.radius):
        ball.p = - ball.p
