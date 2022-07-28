file=open("demo4.txt","a+")
lst=["Hey","Hello","Good night"]
for i in lst:
    file.write(i+"\n")
file.seek(0,0)
print(file.read())

