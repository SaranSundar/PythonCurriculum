
import turtle

a = turtle.Turtle()

# Start
a.pu()
a.goto(-150, -190)
a.pd()
a.begin_fill()

a.left(65)
a.fd(350)
a.seth(185)
a.circle(150, 115)
a.rt(55)
a.fd(30)
a.rt(120)
a.circle(-180, 125)
a.seth(0)
a.left(65)
a.fd(40)
a.seth(0)
a.fd(35)
a.seth(270)
a.fd(50)

a.seth(-20)
a.circle(-175, 180)
a.seth(0)
a.left(65)
a.fd(30)

a.seth(-20)
a.circle(150, 178)
a.seth(270) #down
a.fd(202)
a.seth(135)
a.fd(65)
a.seth(90)  # up
a.fd(112)

a.seth(250)
a.fd(155)       # down and left
a.seth(0)
a.fd(53)

#arrow
a.seth(90)
a.fd(25)
a.seth(-45)
a.fd(60)
a.rt(90)
a.fd(60)
a.seth(90)
a.fd(25)
a.seth(180)
a.fd(68)

a.seth(245)
a.fd(100)
a.seth(180)
a.fd(63)
a.end_fill()



# Extra bit by the arrow
a.pu()
a.goto(27, -132)
a.pd()

a.begin_fill()
a.seth(45)
a.fd(58)
a.seth(270)
a.fd(44)
a.seth(180)
a.fd(44)
a.end_fill()

a.hideturtle()
