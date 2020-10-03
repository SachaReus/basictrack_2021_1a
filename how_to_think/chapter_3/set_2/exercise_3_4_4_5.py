import turtle

window = turtle.Screen()
window.bgcolor("lightblue")

raphael = turtle.Turtle()
raphael.color("hotpink")
raphael.shape("turtle")

# equilateral triangle
for _ in range(3):
    raphael.forward(60)
    raphael.left(120)

# square
for _ in range(4):
    raphael.forward(90)
    raphael.left(90)

# hexagon
for _ in range(6):
    raphael.forward(120)
    raphael.left(60)

# octagon
for _ in range(8):
    raphael.forward(180)
    raphael.left(45)

window.mainloop()
