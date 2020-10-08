import turtle


def draw_star(length):
    for _ in range(5):
        raphael.forward(length)
        raphael.left(144)


window = turtle.Screen()
raphael = turtle.Turtle()

raphael.left(36)

for _ in range(5):

    print(draw_star(100))
    raphael.penup()
    raphael.forward(350)
    raphael.left(144)
    raphael.pendown()

window.mainloop()
