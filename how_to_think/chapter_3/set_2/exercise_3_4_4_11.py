import turtle

window = turtle.Screen()
window.bgcolor("green")
raphael = turtle.Turtle()
raphael.color("blue")
raphael.shape("turtle")

for _ in range(12):
    raphael.penup()
    raphael.forward(70)
    raphael.pendown()
    raphael.forward(20)
    raphael.penup()
    raphael.forward(10)
    raphael.stamp()
    raphael.forward(-100)
    raphael.left(30)

window.mainloop()
