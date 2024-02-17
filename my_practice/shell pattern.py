from turtle import *

bgcolor("light blue")

pensize(3)

pencolor('black')

fillcolor('magenta')

for i in range(9,0,-1):
    begin_fill()
    circle(i*10)
    lt(30)
    end_fill()
    
hideturtle()
mainloop()