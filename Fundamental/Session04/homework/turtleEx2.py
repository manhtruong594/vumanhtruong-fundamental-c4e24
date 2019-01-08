from turtle import *

speed(10)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

for index, colour in enumerate(colors):
    color(colour, colour)

    begin_fill()
    for i in range(2):
        forward(50)
        right(90)
        forward(100)
        right(90)
    forward(50)   
    end_fill() 

mainloop()