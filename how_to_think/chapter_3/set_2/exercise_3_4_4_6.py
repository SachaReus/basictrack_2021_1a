import turtle

window = turtle.Screen()
window.bgcolor("red")
pirate = turtle.Turtle()
pirate.color("black")

angle_of_turn = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for angle in angle_of_turn:
    pirate.forward(100)
    pirate.left(angle)

window.mainloop()

