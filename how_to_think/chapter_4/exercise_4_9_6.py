import turtle

def  draw_poly(t, n, sz):
    for _ in range(sz):
        t.forward(sz)
        t.left(360/n)

def draw_equitriangle(t, sz):
    draw_poly(tess, 3, sz)

window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")

draw_equitriangle(tess, 90)

window.mainloop()
