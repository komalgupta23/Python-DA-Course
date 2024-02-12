from turtle import*
speed("slowest")
pencolor("seagreen")
bgcolor("lightblue")
pensize(3)

for i in range(8):
    fd(100)
    for i in range(8):
        fd(75)
        lt(360/8)
    lt(360/8)
    dot(10)

hideturtle()
mainloop()
