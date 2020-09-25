import turtle

paper = turtle.Screen()
raphael = turtle.Turtle()

colors = ['red', 'orange', 'yellow', 'green', 'blue']

for element in range(12):
    raphael.color(colors[element % 5])
    raphael.forward(50)
    raphael.left(30)

paper.exitonclick()
