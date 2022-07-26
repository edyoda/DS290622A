def student_info():
    rno = int(input("Enter your rno : "))
    name = input("Enter your name : ")
    eng = int(input("Enter your english marks : "))
    maths = int(input("Enter your maths marks : "))
    sci = int(input("Enter your science marks : "))
    total = eng + maths + sci
    out_of = 300
    return total,out_of

def percentage(total_marks,out_of_marks):
    percent = (total_marks/out_of_marks)*100
    return percent

def grading(percentage):
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    else:
        grade = "D"
    return grade

marks,out_of = student_info()
percent = percentage(marks,out_of)
grade = grading(percent)
print(grade)


