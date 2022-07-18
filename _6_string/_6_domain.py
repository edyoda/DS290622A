# lis=input("Enter a string").split("@")
# print("Domain:",lis[1][:-4])


str1 = input("Enter your Email: ")

pos_at = str1.find("@")
pos_dot = str1.find(".",pos_at)

print("Domain name: ",str1[pos_at+1:pos_dot])


mail=input("enter your mail-id :")
a=mail.split('@')
a=a[1].split('.')
print("domain of given mail is ",a[0])

