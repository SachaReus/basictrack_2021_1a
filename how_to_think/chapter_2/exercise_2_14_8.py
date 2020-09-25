time = input("what time is it?")  # in hours
waiting_time = input("how long do you have to wait?")

time_int = int(time)
waiting_time_int = int(waiting_time)

time_alarm_goes_off = (time_int + waiting_time_int)

print("alarm time is:", time_alarm_goes_off)
