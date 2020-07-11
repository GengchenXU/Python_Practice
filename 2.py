import turtle
turtle.speed("fastest")
colors = ["orange","yellow","red","purple","green","blue"]
turtle.pensize(2)
for x in range(1000):
    turtle.color(colors[x % 6])
    turtle.forward(1*x)
    turtle.left(60.5)
