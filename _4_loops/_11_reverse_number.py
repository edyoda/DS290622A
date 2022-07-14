num=int(input("enter a number :")) # 456
rev_no=0
while num>0:
    mod=num%10 #4
    rev_no=( rev_no * 10) + mod # 65*10+4 = 654
    num=num//10 #0
    
print("the reversed no is",rev_no)


lst = [6,7,8,4,2,3,5,5]