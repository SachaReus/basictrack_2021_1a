import turtle


def draw_poly(t, n, sz):
    for _ in range(8):
        t.forward(sz)
        t.left(360/n)


window = turtle.Screen()
window.bgcolor("light-green")
tess = turtle.Turtle()
tess.color("hot-pink")
tess.pensize(5)

draw_poly(tess, 8, 50)

window.mainloop()
