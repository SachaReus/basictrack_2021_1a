day_leaving = int(input("please tell me at what day you are leaving (0-6)"))
holiday_time = int(input("please tell me how many days you are on holiday"))

returning_day = day_leaving + holiday_time

weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print("You will return at:", weekdays[returning_day % 7])
