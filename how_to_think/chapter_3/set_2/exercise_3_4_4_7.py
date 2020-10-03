import turtle

window = turtle.Screen()
window.bgcolor("red")
pirate = turtle.Turtle()
pirate.color("black")

angle_of_turn = [160, -43, 270, -97, -43, 200, -940, 17, -86]

heading = 0
for angle in angle_of_turn:
    pirate.forward(100)
    pirate.left(angle)
    heading += angle

print("final heading of the pirate is", heading % 360)

window.mainloop()