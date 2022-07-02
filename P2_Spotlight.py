
import turtle
import time

wn = turtle.Screen()
wn.title("Spotlight with class")
wn.bgcolor("black")

class Stoplight():
 def __init__(self,x,y):
     # Draw the border
     self.pen = turtle.Turtle()
     self.pen.penup()
     self.pen.hideturtle()
     self.pen.speed(0)
     self.pen.color("yellow")
     self.pen.goto(x-30,y+60)
     self.pen.down()
     self.pen.fd(60)
     self.pen.rt(90)
     self.pen.fd(120)
     self.pen.rt(90)
     self.pen.fd(60)
     self.pen.rt(90)
     self.pen.fd(120)

     self.color = ""

     self.red_light =turtle.Turtle()
     self.yellow_light = turtle.Turtle()
     self.green_light = turtle.Turtle()


     self.red_light.speed(0)
     self.yellow_light.speed(0)
     self.green_light.speed(0)

     self.red_light.color("grey")
     self.yellow_light.color("grey")
     self.green_light.color("grey")

     self.red_light.shape("circle")
     self.yellow_light.shape("circle")
     self.green_light.shape("circle")

     self.red_light.penup()
     self.yellow_light.penup()
     self.green_light.penup()

     self.red_light.goto(x,y+40)
     self.yellow_light.goto(x,y)
     self.green_light.goto(x,y-40)


 def change_color(self, color):
     self.red_light.color("grey")
     self.yellow_light.color("grey")
     self.green_light.color("grey")


     if color == "red":
         self.red_light.color("red")
         self.color = "red"

     elif color =="yellow":
         self.yellow_light.color("yellow")
         self.color="yellow"

     elif color == "green" :
         self.green_light.color("green")
         self.color="green"

     else :
         print("Error : unknown Color {}", format(color))

 def timer(self):
     if self.color == "red" :
         self.change_color("green")
         wn.ontimer(self.timer,4000)

     elif self.color == "yellow":
         self.change_color("red")
         wn.ontimer(self.timer, 3000)

     elif self.color == "green":
         self.change_color("yellow")
         wn.ontimer(self.timer, 2000)



st1 = Stoplight(0,0)
st1.change_color("red")
st1.timer()

st2 = Stoplight(-100,0)
st2.change_color("yellow")
st2.timer()

st3 = Stoplight(100,0)
st3.change_color("green")
st3.timer()



wn.mainloop()


'''
pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.up()
pen.goto(-30,60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)


red_light = turtle.Turtle()
red_light.shape("circle")
red_light.color("grey")
red_light.penup()
red_light.goto(0,40)


yellow_light = turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(0,0)


green_light = turtle.Turtle()
green_light.shape("circle")
green_light.color("grey")
green_light.penup()
green_light.goto(0,-40)




while True :

 red_light.color("red")
 time.sleep(2)

 red_light.color("grey")
 green_light.color("green")
 time.sleep(3)

 green_light.color("grey")
 yellow_light.color("yellow")
 time.sleep(2) '''

'''
import turtle
import time

wn = turtle.Screen()
wn.title("Spotlight")
wn.bgcolor("black")


pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.up()
pen.goto(-30,60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)


red_light = turtle.Turtle()
red_light.shape("circle")
red_light.color("grey")
red_light.penup()
red_light.goto(0,40)


yellow_light = turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(0,0)


green_light = turtle.Turtle()
green_light.shape("circle")
green_light.color("grey")
green_light.penup()
green_light.goto(0,-40)




while True :

 red_light.color("red")
 time.sleep(2)

 red_light.color("grey")
 green_light.color("green")
 time.sleep(3)

 green_light.color("grey")
 yellow_light.color("yellow")
 time.sleep(2)



wn.mainloop() '''