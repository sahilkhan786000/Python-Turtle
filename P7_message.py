import turtle
import time
wn = turtle.Screen()
wn.title("Kamine Dost")
wn.bgcolor("white")


turtle.setup(1000,600)
turtle.bgcolor("black")
turtle.pensize(5)
turtle.speed(1)
turtle.color('white')
turtle.begin_fill()
turtle.fillcolor("red")




turtle.up()

turtle.goto(-150,0)
turtle.down()
turtle.left(180)
turtle.forward(100)
turtle.up()
turtle.backward(50)
turtle.down()
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(50)
turtle.up()
turtle.backward(100)
turtle.down()
turtle.forward(50)
turtle.up()
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.goto(0,0)

# Heart shaped

turtle.left(120)
turtle.forward(80)
turtle.circle(-50, 170)
turtle.setheading(20)
turtle.circle(-50,170)
turtle.goto(0,0)
turtle.right(210)
turtle.end_fill()


turtle.up()
turtle.goto(250,200)
turtle.right(90)
turtle.down()
turtle.forward(150)
turtle.circle(60,180)
turtle.forward(150)



turtle.up()
turtle.goto(-180,-300)
turtle.left(90)
turtle.down()
turtle.forward(40)
turtle.circle(-90,195)
turtle.up()
turtle.goto(-180,-300)
turtle.down()
turtle.left(105)
turtle.forward(50)
turtle.left(90)
turtle.forward(30)

turtle.up()
turtle.goto(-120,-120)
turtle.left(90)
turtle.down()
turtle.forward(130)
turtle.circle(60,180)
turtle.forward(130)

turtle.up()
turtle.goto(50,-120)
turtle.down()
turtle.left(40)
turtle.backward(100)
turtle.right(70)
turtle.backward(140)
turtle.forward(220)


turtle.up()
turtle.left(130)
turtle.goto(270,-130)
turtle.down()
turtle.right(30)
turtle.circle(60,220)
turtle.right(30)
turtle.circle(-60,220)



turtle.mainloop()