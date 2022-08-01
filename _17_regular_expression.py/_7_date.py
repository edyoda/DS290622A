import re
date=input('Enter a date:')
# result=re.findall('^[01-31]{2}[-][01-12]{2}[-][1000-2099]{4}$',date)
result=re.findall("^[0-2][0-9]|[3][0-1][-][0][0-9]|[1][0-2][-][0-9]{4}$",date)

if result:
    print("date is right")
else:
    print('date is worng')




