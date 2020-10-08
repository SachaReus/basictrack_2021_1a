import turtle


def draw_star(length):
    for _ in range(5):
        raphael.forward(length)
        raphael.left(144)


window = turtle.Screen()
raphael = turtle.Turtle()

raphael.left(36)
print(draw_star(100))


window.mainloop()
