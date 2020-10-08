import turtle

def  draw_poly(t, n, sz):
    for _ in range(8):
        t.forward(sz)
        t.left(360/n)

window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

draw_poly(tess, 8, 50)

window.mainloop()
