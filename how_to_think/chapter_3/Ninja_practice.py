import turtle

window = turtle.Screen()
window.bgcolor("lightblue")
window.title("raphael triangle")

raphael = turtle.Turtle()
raphael.color("white")
raphael.pensize(4)
raphael.shape("turtle")
raphael.speed(2)

raphael.forward(80)
raphael.left(120)
raphael.forward(80)
raphael.left(120)
raphael.forward(80)
raphael.left(120)


window.mainloop()