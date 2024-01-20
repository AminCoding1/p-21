import turtle

t = turtle.Turtle()
screen = turtle.Screen()
t.pensize(4)
t.pencolor("red")

def petal():
    t.circle(-121.6, 150)
    t.right(149)
    t.circle(46.08, 90)
    t.circle(-57.6, 100)
    t.circle(47.36, 110)
    t.right(95)
    t.forward(3.84)
    t.right(83)
    t.circle(-96, 70)

def star():
    t.fillcolor("red")
    t.begin_fill()
    for j in range(5):
        t.forward(30)
        t.right(144)
    t.end_fill()

t.penup()

for i in range(5):
    t.forward(6.4)
    t.pendown()
    petal()
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t_direction = 72 * (i + 1)
    t.right(t_direction)

t.setheading(90)

for i in range(5):
    t.forward(118)
    t.pendown()
    star()
    t.penup()
    t.goto(0, 0)
    t.right(72)

t.hideturtle()
screen.exitonclick()
