from turtle import*

def hexagon():      # no arguments
    for _ in range(6):         # use these type of functions when working with global variale
        fd(100)
        lt(60)
                    # no return
        
def pentagon():
    for _ in range(5):
        fd(50)
        lt(72)
        
# testing the functions

for i in range(6):
    fd(100)
    hexagon()
    pentagon()
    lt(60)
    
    
hideturtle()
mainloop()