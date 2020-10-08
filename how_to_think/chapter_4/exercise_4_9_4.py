import turtle

def draw_square (animal):
    for _ in range(4):
        animal.forward(90)
        animal.left(90)

window = turtle.Screen()
window.bgcolor("lightgreen")
raphael = turtle.Turtle()
raphael.color("blue")
raphael.pensize(3)

for _ in range(20):
    draw_square(raphael)
    raphael.left(18)

window.mainloop()