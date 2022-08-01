import re
pan_no=input("Enter PAN number :")
res=re.findall("^[A-Z]{5}[0-9]{4}[A-Z]{1}$",pan_no)
if res:
    print("Correct")
else:
    print("Incorrect")

