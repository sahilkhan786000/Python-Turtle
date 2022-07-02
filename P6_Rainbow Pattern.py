'''import turtle

wn = turtle.Screen()
wn.title("Spotlight with class")
wn.bgcolor("white")
turtle.pensize(5)
turtle.speed(1)
turtle.color('red')
turtle.begin_fill()

turtle.left(90)
turtle.forward(100)
turtle.up()
turtle.backward(100)
turtle.down()
turtle.right(180)
turtle.circle(90,180)
turtle.forward(100)

turtle.mainloop()
'''
import turtle
colors = ["red", "yellow", "green", "violet", "blue", "orange"]
t=turtle.Pen()
turtle.bgcolor("black")
turtle.speed(900)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)



turtle.mainloop()



