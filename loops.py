from turtle import *
speed("slowest")
pencolor("red")
pensize(5)
for i in range(1,5):
    fd(120)
    rt(90)
    write(f'n={1}', font = ("Calibri",16))
''''pencolor("blue")
pensize(5)
fd(120)
lt(90)
fd(120)
rt(90)
fd(120)
rt(90)
fd(120)
rt(90)
fd(120)
rt(90)'''

pencolor("green")
pensize(5)
for i in range(1,9):
    fd(120)
    rt(45)

hideturtle()
mainloop()
