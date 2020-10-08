import turtle

def draw_square(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)

window = turtle.Screen()
window.bgcolor("lightgreen")

raphael = turtle.Turtle()
raphael.shape("arrow")
raphael.color("hotpink")
raphael.pensize(5)

size = 20
for _ in range(5):
    draw_square(raphael, size)
    raphael.penup()
    raphael.forward(40)
    raphael.pendown()

window.mainloop()