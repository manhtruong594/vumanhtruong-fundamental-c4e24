from turtle import *

def draw_square(lenghth, cl):
    color(cl)
    for i in range(4):
        forward(lenghth)
        left(90)
draw_square(100,"red")