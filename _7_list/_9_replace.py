size=int(input("Enter size:"))
lis=[]
for i in range(size):
    value=(input("Enter string"))
    lis.append(value)

old_char=input("Enter old char")
newchar=input("Enter new char")

rep=[]
for i in lis:
    string=""
    for j in i:
        if j==old_char: 
            string = string + newchar
        else:
            string = string + j
    rep.append(string)
print(rep)
