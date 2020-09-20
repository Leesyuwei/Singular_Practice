import turtle

turtle.shape('circle')
turtle.pensize(1)
turtle.penup()
for i in range(5,610,2):
    turtle.forward(i)
    turtle.right(25)
    turtle.stamp()