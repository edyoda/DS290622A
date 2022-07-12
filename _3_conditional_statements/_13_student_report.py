name = input('enter your name: ')
r_no = input('enter your roll no.: ')
eng = int(input('enter your marks: '))
math = int(input('enter your marks: '))
sci = int(input('enter your marks: '))

total = eng+math+sci
print(total)

perc = total*100/300
print(perc)

if perc >= 90:
    print('Grade A')
elif perc >= 80:
    print('Grade B')
elif perc >= 60:
    print('Grade C')
else:
    print('Grade D')
