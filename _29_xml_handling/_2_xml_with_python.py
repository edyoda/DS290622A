from cgitb import html
from bs4 import BeautifulSoup

file = open("B:\\DS290622A\\DS290622A\\_29_xml_handling\\xml_dump.xml","r")
soup = BeautifulSoup(file,'html.parser')
# print(soup)

# find_all is converts data into list
data = soup.find_all("student")
# print(data)

# find is used to fetch the data on the bases of tag_name
name = soup.find("name")
print(name.text)

rno = soup.find("rno")
print(rno.text)

for i in data:
    print(i.find("name").text)

name = soup.find("name",{"name":"three"})
print("Name : ",name.text)