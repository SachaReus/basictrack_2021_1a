mode_of_travel = input("please tell me are you walking, biking or ride a car?")
distance = float(input("please tell me the distance in km"))
time_to_get_going = input("please tell me how long it takes to get going in minutes")
time_to_find_parking = input("please tell me how long it takes to find a parking spot in minutes")

walking_speed = 5  # in km/h
biking_speed = 15  # in km/h
car_speed = 60  # in km/h

hour_time_to_get_going_int = int(time_to_get_going) / 60
hour_time_to_find_parking_int = int(time_to_find_parking) / 60

if mode_of_travel == "walking":
    time = distance / 5
elif mode_of_travel == "biking":
    time = distance / 15
elif mode_of_travel == "ride a car":
    time = distance / 60

hours_to_get_somewhere = (time + hour_time_to_get_going_int + hour_time_to_find_parking_int)
minutes_to_get_somewhere = (hours_to_get_somewhere % 1) * 60

print("hours to get somewhere", hours_to_get_somewhere-(hours_to_get_somewhere % 1))
print("minutes to get somewhere", minutes_to_get_somewhere)
