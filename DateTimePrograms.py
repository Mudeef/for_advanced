import datetime
print("Current date and time: ", datetime.datetime.now())
print("Current Year: ", datetime.date.today().strftime("%Y"))
print("Month of Year: ", datetime.date.today().strftime("%B"))
print("Weak number of the Year: ", datetime.date.today().strftime("%W"))
print("Weekday of the Year: ", datetime.date.today().strftime("%w"))
print("Day of Year: ", datetime.date.today().strftime("%j"))
print("Day of month: ", datetime.date.today().strftime("%d"))
print("Day of weak: ", datetime.date.today().strftime("%A"))
