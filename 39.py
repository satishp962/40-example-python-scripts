import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.pensize(5)

t.penup()
t.setpos((-200, 10))
t.pendown()

t.forward(-50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(-50)
t.left(90)
t.forward(50)
t.left(90)

t.penup()
t.setpos((-80, 10))
t.pendown()

t.forward(150)
t.left(90)
t.forward(50)
t.left(90)
t.forward(150)
t.left(90)
t.forward(50)
t.left(90)

t.penup()
t.setpos((200, 10))
t.pendown()

t.circle(50)

wn.exitonclick()