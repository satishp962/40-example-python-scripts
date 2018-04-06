import turtle

wn = turtle.Screen()
polygon = turtle.Turtle()
polygon.pensize(5)
polygon.penup()
polygon.setpos((-80, 80))
polygon.pendown()

def draw(sides):
    num_sides = sides
    side_length = 60
    angle = 360.0/ num_sides

    for i in range(num_sides):
        polygon.forward(side_length)
        polygon.right(angle)

sides = [3, 4, 6, 8]

x, y = -350, 80
for side in sides:
    polygon.penup()
    x = x + 150
    polygon.setpos((x, y))
    polygon.pendown()
    draw(side)

wn.exitonclick()
