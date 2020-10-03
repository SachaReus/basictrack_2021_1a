mode_of_travel = input("please tell me are you walking, biking or ride a car?")
distance = float(input("please tell me the distance in km"))

walking_speed = 5  # in km/h
biking_speed = 15  # in km/h
car_speed = 60  # in km/h

if mode_of_travel == "walking":
    time = distance / walking_speed
elif mode_of_travel == "biking":
    time = distance / biking_speed
elif mode_of_travel == "ride a car":
    time = distance / car_speed

print("travel time is:", time)


