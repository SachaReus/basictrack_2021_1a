import turtle

window = turtle.Screen()
window.bgcolor("light-green")
raphael = turtle.Turtle()
raphael.color("blue")
raphael.pensize(2)

for i in range(100):
    raphael.forward(i * 5)
    raphael.right(89)

window.mainloop()
