# datetime module - helps to code wrt to date and time
import datetime as dt

current_date = dt.datetime.now()
print(current_date)

print("A : ",current_date.strftime("%A"))

print("a : ",current_date.strftime("%a"))

print("B : ",current_date.strftime("%B"))

print("b : ",current_date.strftime("%b"))

print("C : ",current_date.strftime("%C"))

print("c : ",current_date.strftime("%c"))

print("D : ",current_date.strftime("%D"))

print("d : ",current_date.strftime("%d"))

print("X : ",current_date.strftime("%X"))

print("x : ",current_date.strftime("%x"))

print("S : ",current_date.strftime("%S"))

# year = current_date.year
# print(year)

# month = current_date.month
# print(month)

# day = current_date.day
# print(day)

# hr = current_date.hour
# print(hr)

# mins = current_date.minute
# print(mins)

# sec = current_date.second
# print(sec)

# date = dt.datetime(2022,6,10)
# print(date)

# date = dt.datetime(2022,6,10,1,30)
# print(date)