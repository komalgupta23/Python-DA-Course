from turtle import *

def polygon(side,size,color):
    fillcolor(color)
    begin_fill()
    for _ in range(side):
        fd(size)
        lt(360/side)
    end_fill()
        
        
# testing

for i in range(6):
    fd(100)
    polygon(5, 100,"seagreen")
    polygon(side=10,size=50, color="blue")      #named call
    lt(60)
    
    
hideturtle()
mainloop()