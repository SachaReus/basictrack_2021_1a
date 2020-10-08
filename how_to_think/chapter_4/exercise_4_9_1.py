import turtle


def draw_square(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)


window = turtle.Screen()
window.bgcolor("light-green")

raphael = turtle.Turtle()
raphael.shape("arrow")
raphael.color("hot-pink")
raphael.pensize(5)

size = 20
for _ in range(5):
    draw_square(raphael, size)
    raphael.penup()
    raphael.forward(40)
    raphael.pendown()

window.mainloop()
