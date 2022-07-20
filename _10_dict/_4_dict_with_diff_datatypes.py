dict1 = {
    "name":"Sachin",
    "age":24,
    "male":True,
    "hobbies":["reading","writing","coding"],
    "languages":{1:"Python",2:"Java",3:"PHP"}
}
# print(dict1['hobbies'][2])
print(dict1['languages'][2])

lst = [1,2,4,6,{1:"Bharati"},(4,5,2)]
print(lst[4][1])

dict2 = {
    "student" : {
        "name" : "suraj",
        "days" : {
            "monday" : ["eng","maths","sci"],
            "tuesday" : ["social","evs","history"]
        }
    }
}

print(dict2["student"]["days"]["tuesday"][2])