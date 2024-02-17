from turtle import *

speed(3)
bgcolor('seagreen')
title('My Turtle Program')
shapesize(3)

pensize(5)

circle(50)

dot(5)

goto(-60,50)

fillcolor('lightblue')

begin_fill()
for i in range(4):
    fd(100)
    lt(90)
    
end_fill()

hideturtle()
mainloop()