# # date1=input("Enter the date in dd: ")
# # date2=input("Enter the date in mm: ")
# # date3=input("Enter the date in yyyy: ")
# # dd=int(date1)
# # mm=int(date2)
# # yy=int(date3)

# # if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
# #     max_date=31
# # elif(mm==4 or mm==6 or mm==9 or mm==11):
# #     max_date=30
# # elif(yy%4==0 and yy%100!=0 or yy%400==0):
# #     max_date=29
# # else:
# #     max_date=28
# # if(mm<1 or mm>12):
# #     print("Date is invalid.")
# # elif(dd<1 or dd>max_date):
# #     print("Date is invalid.")


# dd = int(input("Enter the day: "))
# mm = int(input("Enter the month: "))
# yyyy = int(input("Enter the year: "))
# lst1 = [1,3,5,7,8,10,12]
# lst2 = [4,6,9,11]
# while True:
#     if dd > 0 and dd < 31 and (mm in lst2):
#         print("Valid Date")
#         break
#     elif dd > 0 and dd <=28 and  mm == 2:
#         print("Valid Date")
#         break
#     elif dd == 29 and mm == 2 and ((yyyy % 4 ==0 and yyyy % 100 == 0) or yyyy % 400 ==0):
#         print("Valid Date, because it is a leap year")
#         break
#     elif dd > 0 and dd <= 31 and (mm in lst1):
#         print("Valid Date")
#         break
#     else:
#         print("Invalid Date!")
#         break

dd=int(input("Enter Date:"))
mm=int(input("Enter Month:"))
year=int(input("Enter Year:"))
leap=None
dic={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
if year%100==0 and year%400==0 or year%4==0 and year%100 !=0:
    leap=True
else:
    leap=False
if leap:
    dic[2]=29
if (dd<=dic[mm] and dd>0) and (mm<12 and mm>0):
    print("Valid Year")
    if leap:
        print("Leap Year")
    else:
        print("Not Leap Year")
else:
    print("Invalid year")
