import turtle

window = turtle.Screen()
window.bgcolor("yellow")
raphael = turtle.Turtle()
raphael.color("black")

raphael.left(36)
for _ in range(5):
    raphael.forward(100)
    raphael.left(180-36)

window.mainloop()
