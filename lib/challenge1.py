# Converting 12-hour time to 24-hour time

def time_conversion(hours, minutes, period):
    if period == "AM" or period == "am" and hours == 12:
        hour = "00"
    elif hours > 10:
        hour = f"{hours}"
    else:
        hour = f'0{hours}'
    
    if (period == "PM" or period == "pm"):
        hour = "12"
    if hours == 12:
            hour = f"{hours}"
    else:
            hour = hours + 12

    time = f'Time in 24-hour: {hour}{minutes:02d}'
    return time

print(time_conversion(8, 30, "pm"))
# print(time_conversion(8, 30, "pm"))
# print(time_conversion(8, 30, "am"))
# print(time_conversion(12, 0, "am"))
# print(time_conversion(12, 15, "am"))

