def hours2days(hours):
    days = hours // 24  # get number of days by dividing hours by 24
    _hours = hours % 24 # get hours by hours modulo 24
    return days, _hours


print(hours2days(39))
