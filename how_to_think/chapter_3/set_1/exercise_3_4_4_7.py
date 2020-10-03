# calculating the hypotenuse: A**2 + B**2 = C**2
# length hypotenuse = C**0.5

length_A = float(input("please give me the length of side A"))
length_B = float(input("Please give me the length of side B"))

C_square = float(length_A) ** 2 + float(length_B) ** 2

length_hypotenuse = float(C_square) ** 0.5

print("Length of the hypotenuse is:", length_hypotenuse)
