import datetime
print("Current date and time: ", datetime.datetime.now())
print("Current Year: ", datetime.date.today().strftime("%Y"))
print("Month of Year: ", datetime.date.today().strftime("%B"))
print("Weak number of the Year: ", datetime.date.today().strftime("%W"))
print("Weekday of the Year: ", datetime.date.today().strftime("%w"))
print("Day of Year: ", datetime.date.today().strftime("%j"))
print("Day of month: ", datetime.date.today().strftime("%d"))
print("Day of weak: ", datetime.date.today().strftime("%A"))

# print("==============================================================")

# import datetime
# today = datetime.date.today()
# yesterday = today - datetime.timedelta(days = 1)
# tomorrow = today + datetime.timedelta(days = 1)
# print('Yesterday : ',yesterday)
# print('Today :',today)
# print('Tomorrow :',tomorrow)
#
# print("=====================================================")
# from datetime import date, timedelta
#
# def all_sundays(year):
#     dt = date(year, 1, 1)
#     dt += timedelta(days=6 - dt.weekday())
#     while dt.year == year:
#         yield dt
#         dt += timedelta(days=7)
#
# for s in all_sundays(2020):
#     print(s)

print("================================================")

from datetime import date
a = date(2000,2,28)
b = date(2001,2,28)
print(b-a)
