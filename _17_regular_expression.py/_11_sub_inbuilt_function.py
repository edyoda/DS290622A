import re

mobile_no = "913-789 8948" #9137898948
result = re.sub("\D","",mobile_no)
print(result)

data = "1800 0002 2020" #18 2 22
result= re.sub("0","",data)
print(result)

data = "Python" # @P@y@t@h@o@n@
result = re.sub("","@",data)
print(result)
