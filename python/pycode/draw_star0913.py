import turtle

turtle.shape('circle')
turtle.pensize(5)
turtle.pencolor('yellow')
turtle.color('yellow')
turtle.begin_fill()
for i in range(5):
    turtle.forward(100)
    turtle.right(144)
    turtle.stamp()
turtle.fillcolor('yellow')
turtle.end_fill()