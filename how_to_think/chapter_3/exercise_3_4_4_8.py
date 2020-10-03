# for right-angled triangle: A**2 + B**2 = C**2 must hold up

length_A = int(input("please give me the length of side A"))
length_B = int(input("please give me the length of side B"))
length_C = int(input("please give me the length of side C"))

if (int(length_A) ** 2 + int(length_B) ** 2) == int(length_C) ** 2:
    print("True, the triangle is right-angled")
else:
    print("False, the triangle is not right-angled")


